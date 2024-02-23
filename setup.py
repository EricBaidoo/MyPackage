from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='01.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='Eric Baidoo',
    author_email='<kbaidu7@gmail.com>'
)
