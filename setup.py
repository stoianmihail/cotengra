from setuptools import setup, find_packages
from os import path
import versioneer

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cotengra',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='opt_einsum compatible contractors for large tensor networks',
    long_description=long_description,
    url='https://github.com/jcmgray/cotengra',
    author='Johnnie Gray',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='tensor network contraction graph hypergraph partition einsum',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'opt_einsum',
        'tqdm',
        'cytoolz',
        'optuna',
        'autoray',
    ],
    extras_require={
        'recommended': [
            'kahypar',
            'optuna',
            'networkx',
            'autoray',
            'ray',
        ],
        'docs': [
            'sphinx>=2.0',
            'sphinx-autoapi',
            'sphinx-copybutton',
            'myst-nb',
            'furo',
            'setuptools_scm',
            'ipython!=8.7.0',
        ],
        'test': [
            'numpy',
            'kahypar',
            'matplotlib',
            'networkx'
            'altair',
            'seaborn',
            'pytest',
            'dask',
            'distributed',
            'baytune',
            'skopt',
            'chocolate',
            'nevergrad',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/jcmgray/cotengra/issues',
        'Source': 'https://github.com/jcmgray/cotengra/',
    },
    include_package_data=True,
)
