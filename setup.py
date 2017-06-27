from setuptools import setup

setup(name="hello",
      version='0.0.3',
      packages=["hello"],
      entry_points = {
          'console_scripts': ['hello=hello:hello']
      },
      install_requires=['colorama']
      )
