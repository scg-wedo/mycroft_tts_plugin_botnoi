#!/usr/bin/env python3

from os.path import join, abspath, dirname
from setuptools import setup

with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    requirements = f.readlines()

PLUGIN_ENTRY_POINT = 'botnoi_tts_plug = mycroft_tts_plugin_botnoi:botnoiTTSPlugin'
setup(
    name='mycroft-tts-plugin-botnoi',
    version='0.1',
    description='Botnoi tts plugin for mycroft',
    url='https://github.com/SCGWEDOtech/mycroft_tts_plugin_botnoi.git',
    author='Natchanon Pornprasatpol',
    author_email='natchpor@scg.com',
    license='Apache-2.0',
    packages=['mycroft_tts_plugin_botnoi'],
    # install_requires=requirements,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft plugin tts',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)