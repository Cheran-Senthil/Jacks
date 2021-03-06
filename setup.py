from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='Jacks',
    version='0.1.1',
    description='Basic Commands for Poker',
    long_description_content_type='text/markdown',
    long_description=readme(),
    url='https://github.com/Cheran-Senthil/Jacks',
    author='Cheran and Mukundan',
    license='MIT',
    packages=['jacks'],
    install_requires=[
        'six',
        'termcolor',
    ])
