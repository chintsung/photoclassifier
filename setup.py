import setuptools

from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

description = ''.join(['Help users to classify photos by date.',])

setup(name='photoclassifier',
      version='0.1',
      description=description,
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent',
      ],
      url='',
      author='Kendrick Tseng',
      author_email='chichon.tw@gmail.com',
      license='',
      packages=setuptools.find_packages(),
      package_data={},
      install_requires=[
      ],
      dependency_links=[
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      py_modules=[
      ],
      zip_safe=False)
