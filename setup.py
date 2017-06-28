from distutils.core import Extension
try:
    from setuptools import setup
except ImportError:
    from distutils import setup
    
#  from Cython.Build import cythonize


LONG_DESCRIPTION = """`pycsa` is a Python implementation of coupled simulated 
annealing (CSA). The original papar can be found 
[here](ftp://ftp.esat.kuleuven.be/sista/sdesouza/papers/CSA2009accepted.pdf).

Essentially, CSA is like multiple simulated annealing (i.e. m independent SA 
processes run in parallel), except that the acceptance probability at each step 
is calculated as a function of the current state across all m processes.
"""

setup(
    name="csa",
    version="0.1",
    description="Python implementation of coupled simulated annealing (CSA)",
    long_description=LONG_DESCRIPTION,
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
