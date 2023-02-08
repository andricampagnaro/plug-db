from setuptools import setup, find_packages

setup(
    name='plug_db',
    version='0.1.0',
    description='Easy way to connect in a container database',
    author='Andrieli Campagnaro',
    author_email='andricampagnaro@gmail.com',
    packages=find_packages(),
    install_requires=[
        'loguru',
        'pandas',
        'psycopg2-binary',
        'sqlalchemy'
    ],
)
