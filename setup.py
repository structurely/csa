from Cython.Build import cythonize
try:
    from setuptools import setup,Extension
except ImportError:
    from distutils.core import setup,Extension
    
ext_modules = [Extension("pycsa",
                         sources=["csa/optimize.pyx"],
                         libraries=["m"])]   

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
    ext_modules=cythonize(ext_modules),
    keywords=[
        "csa",
        "sa",
        "simulated annealing",
        "annealing",
        "coupled simulated annealing",
    ],
    classifiers=[],
)
