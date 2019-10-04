from setuptools import setup, find_packages


setup(
    name='pyfatal_cassandra',
    version='0.0.1',
    author='Lounis Rahmani',
    author_email='lrahmani@fluksaqua.com',
    description='Cassanda Tools And Library',
    long_description='',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['cassandra-driver>=3.18.0'],
)
