from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy as np

setup(
    name = "csa",
    packages=["csa"],
    package_dir={"csa": "csa"},
    ext_modules = cythonize("csa/cost_eval.pyx"),
    include_dirs=[np.get_include()],
    #  ext_modules=[
        #  Extension("csa", ["cost_eval.pyx"],
                  #  include_dirs=[np.get_include()]),
    #  ],
)
