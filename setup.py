import setuptools
from setuptools import setup
import sys

setup(
    name='Vmanager',
    version='0.1',
    description='A cross platform version management tool.',
    author='Amirreza Zahraei',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
    ],
    keywords="version, version management, version comparison, packaging, latest version",
    author_email='amir.reza.zahraei@gmail.com',
    url='https://github.com/AmirrezaZahraei1387/PyVersion',
    packages=setuptools.find_packages()
)
