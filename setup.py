from setuptools import setup

with open('README.md') as file:
    long_description = file.read() 
  
  
# specify requirements of your package here 
REQUIREMENTS = ['pyperclip'] 
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python', 
    'Programming Language :: Python :: 2', 
    'Programming Language :: Python :: 2.6', 
    'Programming Language :: Python :: 2.7', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.3', 
    'Programming Language :: Python :: 3.4', 
    'Programming Language :: Python :: 3.5', 
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',  
    ] 
  
# calling the setup function  
setup(name='codesnip',
      version='0.0.2',
      description='A small program for storing and managing your code snippets.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      py_modules = ["codesnipp"],
      package_dir = {'': 'src'},
      entry_points ={
          'console_scripts': [
              'codesnippet = vibhu4gfg.gfg:main'
          ]
      },
      url='https://github.com/sarveshbhatnagar/codesnip',
      author='Sarvesh Bhatnagar', 
      author_email='sarveshbhatnagar08@gmail.com', 
      license='MIT', 
      packages=['codesnipp'],
      classifiers=CLASSIFIERS, 
      install_requires=REQUIREMENTS, 
      keywords='snippet management code save'
      ) 
