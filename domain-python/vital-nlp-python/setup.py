from setuptools import setup, find_packages

setup(
    name='vital-ai-nlp',
    version='0.1.6',
    author='Marc Hadfield',
    author_email='marc@vital.ai',
    description='VitalSigns nlp domain',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vital-ai/vitalhome-aimp',
    packages=find_packages(),
    entry_points={
        'vitalsigns_packages': [
            'com_vitalai_domain_nlp = com_vitalai_domain_nlp'
        ]
    },
    package_data={
        '': ['*.pyi'],
        'com_vitalai_domain_nlp': ['domain-ontology/*.owl']
    },
    license='Apache License 2.0',
    install_requires=[
            'vital-ai-domain>=0.1.9',
        ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
