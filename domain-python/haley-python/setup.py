from setuptools import setup, find_packages

setup(
    name='vital-ai-haley',
    version='0.1.9',
    author='Marc Hadfield',
    author_email='marc@vital.ai',
    description='VitalSigns haley domain',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vital-ai/vitalhome-haley',
    packages=find_packages(),
    entry_points={
        'vitalsigns_packages': [
            'com_vitalai_haley_domain = com_vitalai_haley_domain'
        ]
    },
    package_data={
        '': ['*.pyi'],
        'com_vitalai_haley_domain': ['domain-ontology/*.owl']
    },
    license='Apache License 2.0',
    install_requires=[
            'vital-ai-aimp>=0.1.17',
        ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
