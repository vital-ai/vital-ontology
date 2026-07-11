"""Migrate each domain package's setup.py to pyproject.toml (Phase 5).

Parses the (templated) setup.py of every package, writes an equivalent
pyproject.toml (setuptools backend), and removes setup.py. Idempotent:
skips packages that already have pyproject.toml.

Usage: python tools/migrate_pyproject.py
"""

import ast
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PACKAGE_DIRS = ['vital-domain-python'] + [
    os.path.join('domain-python', d)
    for d in sorted(os.listdir(os.path.join(REPO_ROOT, 'domain-python')))
    if os.path.isdir(os.path.join(REPO_ROOT, 'domain-python', d))
]


def parse_setup(path):
    """Extract the setup(...) keyword arguments as python values."""
    with open(path) as f:
        tree = ast.parse(f.read())

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and \
                getattr(node.func, 'id', '') == 'setup':
            kwargs = {}
            for kw in node.keywords:
                try:
                    kwargs[kw.arg] = ast.literal_eval(kw.value)
                except ValueError:
                    # non-literal (find_packages(...), open(...).read())
                    kwargs[kw.arg] = ast.unparse(kw.value)
            return kwargs
    raise ValueError(f'no setup() call found in {path}')


def toml_str(value):
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'


def toml_list(values, indent='    '):
    if not values:
        return '[]'
    items = ',\n'.join(indent + toml_str(v) for v in values)
    return '[\n' + items + ',\n]'


def render(kwargs):
    name = kwargs['name']
    version = kwargs['version']
    description = kwargs.get('description', '')
    url = kwargs.get('url', '')
    requires = kwargs.get('install_requires', [])
    python_requires = kwargs.get('python_requires', '>=3.10')
    classifiers = kwargs.get('classifiers', [])
    entry_points = kwargs.get('entry_points', {})
    package_data = kwargs.get('package_data', {})

    # find_packages(exclude=[...]) -> exclude list
    find_packages_src = kwargs.get('packages', 'find_packages()')
    excludes = []
    if 'exclude=' in find_packages_src:
        excludes = ast.literal_eval(
            find_packages_src.split('exclude=', 1)[1].rstrip(')'))

    lines = []
    lines.append('[build-system]')
    lines.append('requires = ["setuptools>=68"]')
    lines.append('build-backend = "setuptools.build_meta"')
    lines.append('')
    lines.append('[project]')
    lines.append(f'name = {toml_str(name)}')
    lines.append(f'version = {toml_str(version)}')
    lines.append(f'description = {toml_str(description)}')
    lines.append('readme = "README.md"')
    lines.append('license = {text = "Apache License 2.0"}')
    lines.append('authors = [{name = "Marc Hadfield", '
                 'email = "marc@vital.ai"}]')
    lines.append(f'requires-python = {toml_str(python_requires)}')
    lines.append(f'classifiers = {toml_list(classifiers)}')
    lines.append(f'dependencies = {toml_list(requires)}')
    lines.append('')
    lines.append('[project.urls]')
    lines.append(f'Homepage = {toml_str(url)}')

    for group, entries in entry_points.items():
        lines.append('')
        lines.append(f'[project.entry-points.{toml_str(group)}]')
        for entry in entries:
            key, _, target = [p.strip() for p in entry.partition('=')]
            lines.append(f'{toml_str(key)} = {toml_str(target)}')

    lines.append('')
    lines.append('[tool.setuptools.packages.find]')
    if excludes:
        lines.append(f'exclude = {toml_list(excludes)}')
    else:
        lines.append('exclude = []')

    if package_data:
        lines.append('')
        lines.append('[tool.setuptools.package-data]')
        for pkg, globs in package_data.items():
            key = toml_str(pkg) if pkg else '"*"'
            lines.append(f'{key} = {toml_list(globs)}')

    lines.append('')
    return '\n'.join(lines)


def main():
    for rel_dir in PACKAGE_DIRS:
        pkg_dir = os.path.join(REPO_ROOT, rel_dir)
        setup_path = os.path.join(pkg_dir, 'setup.py')
        pyproject_path = os.path.join(pkg_dir, 'pyproject.toml')

        if os.path.exists(pyproject_path):
            print(f'skip (exists): {rel_dir}/pyproject.toml')
            continue
        if not os.path.exists(setup_path):
            print(f'skip (no setup.py): {rel_dir}')
            continue

        kwargs = parse_setup(setup_path)
        content = render(kwargs)

        with open(pyproject_path, 'w') as f:
            f.write(content)
        os.remove(setup_path)
        print(f'migrated: {rel_dir} ({kwargs["name"]} {kwargs["version"]})')


if __name__ == '__main__':
    sys.exit(main())
