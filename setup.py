from distutils.core import Extension
try:
    from setuptools import setup
except ImportError:
    from distutils import setup
    
#  from Cython.Build import cythonize


setup(
    name="pycsa",
    version="0.1.2",
    description="Python implementation of coupled simulated annealing (CSA)",
    long_description=open("README.rst").read(),
    author="Boudhayan Banerjee, Evan 'Pete' Walsh",
    author_email="ronnie@structurely.com, epwalsh@structurely.com",
    url="https://github.com/structurely/csa",
    packages=["pycsa"],
    package_dir={"pycsa": "csa"},
    #  ext_modules = cythonize("csa/cost_eval.pyx"),
    #  include_dirs=[],
    keywords=[
        "csa",
        "sa",
        "simulated annealing",
        "annealing",
        "coupled simulated annealing",
    ],
    classifiers=[],
)
