"""Compare vitalsigns-generated python code against the committed
(Groovy-generated) code in domain-python/.

Usage:
    python tools/compare_generated.py <domain>              # e.g. haley-taxonomy-python
    python tools/compare_generated.py <domain> --show-diffs # print unified diffs

Compares file sets and contents between build/generated/<domain>/<package>/
and domain-python/<domain>/<package>/. Classification per file:
  IDENTICAL - byte-identical
  COSMETIC  - identical after normalization (whitespace, blank lines)
  SEMANTIC  - differs after normalization

Exit code 0 if all files identical/cosmetic and file sets match, 1 otherwise.
"""

import argparse
import difflib
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

IGNORED = {".DS_Store", "__pycache__"}


def find_package_dir(base: Path) -> Path:
    """Find the single python package dir (contains model/) under base."""
    candidates = [d for d in base.iterdir()
                  if d.is_dir() and (d / "model").is_dir()]
    if len(candidates) != 1:
        raise RuntimeError(f"Expected 1 package dir under {base}, "
                           f"found: {[c.name for c in candidates]}")
    return candidates[0]


def list_files(base: Path):
    return {
        str(p.relative_to(base)): p
        for p in base.rglob("*")
        if p.is_file() and not any(part in IGNORED for part in p.parts)
    }


def normalize(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    # drop leading/trailing blank lines and collapse runs of blanks
    out = []
    for line in lines:
        if line == "" and (not out or out[-1] == ""):
            continue
        out.append(line)
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("domain", help="domain dir name, e.g. haley-taxonomy-python")
    parser.add_argument("--generated-base",
                        default=str(REPO_ROOT / "build" / "generated"))
    parser.add_argument("--show-diffs", action="store_true")
    parser.add_argument("--max-diff-lines", type=int, default=40)
    args = parser.parse_args()

    generated_root = Path(args.generated_base) / args.domain
    committed_root = REPO_ROOT / "domain-python" / args.domain
    if not committed_root.is_dir():
        # packages distributed from the repo root (e.g. vital-domain-python)
        committed_root = REPO_ROOT / args.domain

    gen_pkg = find_package_dir(generated_root)
    com_pkg = find_package_dir(committed_root)

    if gen_pkg.name != com_pkg.name:
        print(f"PACKAGE NAME MISMATCH: generated={gen_pkg.name} "
              f"committed={com_pkg.name}")

    gen_files = list_files(gen_pkg)
    com_files = list_files(com_pkg)

    gen_only = sorted(set(gen_files) - set(com_files))
    com_only = sorted(set(com_files) - set(gen_files))
    common = sorted(set(gen_files) & set(com_files))

    identical, cosmetic, semantic = [], [], []

    for rel in common:
        gen_text = gen_files[rel].read_text()
        com_text = com_files[rel].read_text()
        if gen_text == com_text:
            identical.append(rel)
        elif normalize(gen_text) == normalize(com_text):
            cosmetic.append(rel)
        else:
            semantic.append(rel)

    print(f"=== {args.domain} ({gen_pkg.name}) ===")
    print(f"files: generated={len(gen_files)} committed={len(com_files)} "
          f"common={len(common)}")
    print(f"IDENTICAL: {len(identical)}  COSMETIC: {len(cosmetic)}  "
          f"SEMANTIC: {len(semantic)}")

    if gen_only:
        print(f"\nOnly in GENERATED ({len(gen_only)}):")
        for rel in gen_only:
            print(f"  {rel}")
    if com_only:
        print(f"\nOnly in COMMITTED ({len(com_only)}):")
        for rel in com_only:
            print(f"  {rel}")

    if cosmetic:
        print(f"\nCOSMETIC diffs:")
        for rel in cosmetic:
            print(f"  {rel}")

    if semantic:
        print(f"\nSEMANTIC diffs:")
        for rel in semantic:
            print(f"  {rel}")
        if args.show_diffs:
            for rel in semantic:
                print(f"\n--- committed/{rel}\n+++ generated/{rel}")
                diff = list(difflib.unified_diff(
                    com_files[rel].read_text().splitlines(),
                    gen_files[rel].read_text().splitlines(),
                    lineterm="", n=1))
                for line in diff[2:args.max_diff_lines + 2]:
                    print(line)
                if len(diff) > args.max_diff_lines + 2:
                    print(f"... ({len(diff) - args.max_diff_lines - 2} more lines)")

    ok = not gen_only and not com_only and not semantic
    print(f"\nRESULT: {'PARITY (identical/cosmetic only)' if ok else 'DIFFERS'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
