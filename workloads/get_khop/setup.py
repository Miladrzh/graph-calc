#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


module = Extension(
       '_GetKHopBenchmark',
       sources=[
              'GetKHopBenchmark_wrap.cxx', 
              'GetKHopBenchmark.cpp',
              'orderings.cpp'
       ],
       extra_compile_args=['-std=c++17']
)

setup (name = 'GetKHopBenchmark',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [module],
       py_modules = ["GetKHopBenchmark"],
       )