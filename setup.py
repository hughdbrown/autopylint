""" setup for for autopylint """
#!/usr/bin/env python

from setuptools import setup, find_packages


def reqs_from_file(filename):
    """ Read the setup requirements from a requirements file """
    with open(filename) as f:
        lineiter = (line.rstrip() for line in f if not line.startswith("#"))
        return list(filter(None, lineiter))


setup(
    name='autopylint',
    version='0.0.3',
    description='Tool for automatically applying fixes to errors/warnings identified by pylint',
    author='Hugh Brown',
    author_email='hughdbrown@yahoo.com',

    # Required packages
    install_requires=reqs_from_file('requirements.txt'),
    tests_require=reqs_from_file('test-requirements.txt'),

    # Main packages
    packages=find_packages(),
    zip_safe=False,

    entry_points={
        'console_scripts': [
            # Python modifiers
            'autopylint=src.autopylint:main',
        ],
    },
)
