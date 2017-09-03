from setuptools import setup

setup(name='pykarma',
      version='1.2',
      description="A python API for Karma Decay",
      url='http://github.com/samj1912/pykarma',
      author='Sambhav Kothari',
      author_email='sambhavs.email@gmail.com',
      license='MIT',
      packages=['pykarma'],
      install_requires=[
          'praw',
          'beautifulsoup4',
      ])
