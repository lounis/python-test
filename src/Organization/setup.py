from setuptools import setup, find_packages

setup(
    name="pyfatal_organization",
    version="0.0.1",
    author="Lounis Rahmani",
    author_email="lrahmani@fluksaqua.com",
    description="Organization Tools And Library",
    long_description="",
    packages=find_packages(),
    zip_safe=False,
    install_requires = ['pyfatal_cassandra @ git+https://github.com/lounis/python-test.git@0.0.1#egg=pyfatal_cassandra&subdirectory=src/DB/Cassandra',],
    include_package_data=True,
)
