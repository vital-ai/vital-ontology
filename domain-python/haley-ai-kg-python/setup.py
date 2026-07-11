from setuptools import setup, find_packages

setup(
    name='vital-ai-haley-kg',
    version='0.1.25',
    author='Marc Hadfield',
    author_email='marc@vital.ai',
    description='VitalSigns haley kg domain',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vital-ai/vitalhome-haley',
    packages=find_packages(),
    entry_points={
        'vitalsigns_packages': [
            'ai_haley_kg_domain = ai_haley_kg_domain'
        ]
    },
    package_data={
        '': ['*.pyi'],
        'ai_haley_kg_domain': ['domain-ontology/*.owl']
    },
    license='Apache License 2.0',
    install_requires=[
            'vital-ai-haley>=0.1.9',
            'vital-ai-haley-question>=0.1.7',
            'vital-ai-vitalsigns>=0.1.54'
        ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
