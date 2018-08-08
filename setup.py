# -*- coding: utf-8 -*-
from glob import glob
from os import path as osp
from setuptools import setup, find_packages


proj_dir = osp.dirname(__file__)
modules = [osp.splitext(osp.basename(path))[0]
           for path in glob(osp.join(proj_dir, 'src/*.py'))]
setup(
    name='inkbot',
    version='0.0.2',
    description='Invoke tasks and CLI to backup and restore darknodes',
    license='MIT',
    author='Chew Boon Aik',
    author_email='bachew@gmail.com',
    url='https://github.com/bachew/inkbot',
    download_url='https://github.com/bachew/inkbot/archive/master.zip',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=modules,
    install_requires=[
        "invoke>=1.1.1"
    ],
    zip_safe=False,
    include_package_data=True,  # see MANIFEST.in
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'inkbot=inkbot.cli:main',
        ],
    },
)
