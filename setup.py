#from distutils.extension import Extension
#from distutils.core import setup
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy
import glob, os

from numpy.compat import py3k
try:
      os.remove("pypowspec/src/pypowspec.c")
except: pass
includes = [numpy.get_include(), '/usr/include', 'pypowspec/etc', 'pypowspec/io', 'pypowspec/lib', 'pypowspec/math', 'pypowspec/src']
sources = glob.glob(f"pypowspec/io/*.c") + glob.glob(f"pypowspec/lib/*.c") + glob.glob(f"pypowspec/math/*.c") + glob.glob(f"pypowspec/src/*.c")
pypowspec = Extension("pypowspec",
                  sources=['pypowspec/src/pypowspec.pyx'] + sources,
                  include_dirs=[f"{os.environ.get('FFTW_DIR')}/../include", f"{os.environ.get('FFTW_DIR')}/include"] + includes,
                  library_dirs=[f"{os.environ.get('FFTW_DIR')}", f"{os.environ.get('FFTW_DIR')}/lib"],
                  language='c',
                  extra_compile_args=["-DOMP", "-fopenmp", "-lfftw3_omp"],
                  extra_link_args=["-fopenmp", "-lfftw3_omp"]
             )


setup(name='pypowspec',
      ext_modules=cythonize([pypowspec]),
      packages=['pypowspec'])
