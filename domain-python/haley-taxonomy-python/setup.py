from setuptools import setup, find_packages

setup(
    name='vital-ai-haley-taxonomy',
    version='0.1.7',
    author='Marc Hadfield',
    author_email='marc@vital.ai',
    description='VitalSigns haley taxonomy domain',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vital-ai/vitalhome-haley',
    packages=find_packages(),
    entry_points={
        'vitalsigns_packages': [
            'com_vitalai_haley_taxonomy_domain = com_vitalai_haley_taxonomy_domain'
        ]
    },
    package_data={
        '': ['*.pyi'],
        'com_vitalai_haley_taxonomy_domain': ['domain-ontology/*.owl']
    },
    license='Apache License 2.0',
    install_requires=[
        'vital-ai-haley>=0.1.9'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
