import imp

from setuptools import find_packages, setup

version = imp.load_source('entrofy.version', 'entrofy/version.py')

setup(
    name='entrofy',
    version=version.version,
    description='Entrofy',
    author='Daniela Huppenkothen',
    author_email='daniela.huppenkothen@nyu.edu',
    url='http://github.com/dhuppenkothen/entrofy',
    download_url='http://github.com/dhuppenkothen/entrofy/releases',
    packages=find_packages(),
    long_description="""Entrofy""",
    classifiers=[
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license='ISC',
    install_requires=[
        'pandas>=0.18',
        'numpy>=1.10',
        'seaborn>=0.6.0',
        'matplotlib>=1.4.3',
        'future',
    ],
    extras_require={
        'docs': ['numpydoc']
    }
)
