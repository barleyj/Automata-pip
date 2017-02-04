from setuptools import setup

# specify requirements of your package here
REQUIREMENTS = ['wordster']

# some more details
CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Operating System :: POSIX'
    ]

# calling the setup function 
setup(name='python-automata',
      version='0.0.1',
      description='A personal assistant with pluggable modules',
      long_description=open('README.md').read(),
      url='https://github.com/rahulxxarora/Automata-pip',
      author='Rahul Arora',
      author_email='coderahul94@gmail.com',
      license='MIT',
      packages=['automata', 'automata/modules'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='automata, personal assistant, ML'
      )