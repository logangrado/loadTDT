from setuptools import setup

setup(name         = 'loadTDT',
      version      = '0.1',
      description  = 'Read a TDT tank into a python dictionary',
      url          = '',
      author       = 'Logan Grado',
      author_email = 'grado@umn.edu',
      license      = 'MIT',
      packages     = ['loadTDT'],
      zip_safe     = False,
      install_requires = [
          'numpy'
      ])
