from setuptools import setup

setup(name="hello",
      version='0.0.5',
      description="Say high to the world",
      long_description="A demonstration of python packaging with setup.py",
      classifiers=[
          'Development Status :: 3 - ALpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Topic :: Text Processing :: Linguistic'
      ],
      keywords='tutorial pysprings color',
      url="http://meetup.com/pysprings",
      author="PySprings",
      author_email="pysprings@pysprings.com",
      license="MIT",
      packages=["hello"],
      entry_points = {
          'console_scripts': ['hello=hello:hello']
      },
      install_requires=['colorama'],
      include_package_data=True,
      setup_requires=['pytest-runner'],
      tests_require=['pytest']
      )
