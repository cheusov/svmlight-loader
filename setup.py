from distutils.core import setup, Extension
import numpy as np

ext = Extension('_svmlight_loader',
                include_dirs = [np.get_include(),'.'],
                extra_compile_args=['-O3'],
                sources = ['_svmlight_loader.cpp'])

setup (name = 'svmlight-loader',
       version = '0.1',
       description = 'Fast loader for the svmlight/libsvm sparse data format.',
       author = 'Mathieu Blondel, Lars Buitinck ',
       author_email = 'mathieu@mblondel.org, L.J.Buitinck@uva.nl',
       url = 'https://github.com/mblondel/svmlight-loader',
       license = 'Simple BSD',
       ext_modules = [ext],
       py_modules = ['svmlight_loader',],
       install_requires = ['numpy', 'scipy'])
