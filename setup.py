from distutils.core import Extension
from Cython.Build import cythonize
try:
    from setuptools import setup
except ImportError:
    from distutils import setup

setup(
    name = "csa",
    packages=["csa"],
    package_dir={"csa": "csa"},
    #  ext_modules = cythonize("csa/cost_eval.pyx"),
    #  include_dirs=[],
)
