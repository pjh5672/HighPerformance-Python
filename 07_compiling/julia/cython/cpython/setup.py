from distutils.core import setup

from Cython.Build import cythonize
setup(ext_modules=cythonize("cythonfn5.pyx", compiler_directives={"language_level": "3"}))