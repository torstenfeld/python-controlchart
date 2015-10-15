from setuptools import setup

VERSION = '0.1.5'

setup(
    name='python-controlchart',
    packages=['controlchart'],
    version=VERSION,
    description='Creation of control charts with matplotlib',
    author='Torsten Feld',
    author_email='torsten@torsten-feld.de',
    url='https://github.com/torstenfeld/python-controlchart',
    download_url='https://github.com/torstenfeld/python-controlchart/tarball/' + VERSION,
    keywords=['statistics', 'spc', 'chart', 'tool', 'process control', 'shewhart', 'control chart'],
    requires=['numpy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry'
    ],
)

