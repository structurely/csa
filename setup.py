from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_modules = [Extension("csa",
                         sources=["csa/optimize.pyx"],
                         libraries=["m"])]
setup(
    name="csa",
    packages=["csa"],
    package_dir={"csa": "csa"},
    ext_modules=cythonize(ext_modules)
)
