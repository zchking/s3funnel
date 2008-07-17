from setuptools import setup, find_packages
import sys, os

version = '0.6'

setup(name='s3funnel',
      version=version,
      description="Multithreaded tool for performing operations on Amazon's S3",
      long_description="""\
This tool uses the workerpool for multithreading and boto for access to the Amazon S3 API.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Andrey Petrov',
      author_email='andrey.petrov@shazow.net',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'boto','workerpool >= 0.9.2',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      scripts=['scripts/s3funnel'],
      )
