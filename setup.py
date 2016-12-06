# -*- coding: utf-8 -*-

import os
__DIR__ = os.path.abspath(os.path.dirname(__file__))
import codecs
from setuptools import setup

import tornado_restful


def read(filename):

    return codecs.open(os.path.join(__DIR__, filename), 'r').read()


install_requires = read('requirements.txt').split()


setup(
    name='Tornado-Restful',
    version=tornado_restful.__version__,
    url='https://github.com/iceihehe/tornado-restful',
    license='MIT License',
    author='iceihehe',
    packages=['tornado_restful'],
    install_requires=install_requires,
)
