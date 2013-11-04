import os
from setuptools import setup, find_packages

setup(name='mphello',
      version = '0.1dev',
      description="Morepath Hello World app",
      author="Martijn Faassen",
      author_email="faassen@startifact.com",
      license="BSD",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'morepath'
        ],
      )
