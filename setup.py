try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(
    name="pycsa",
    version="0.1.3",
    description="Python implementation of coupled simulated annealing (CSA)",
    long_description=open("README.rst").read(),
    author="Boudhayan Banerjee, Evan 'Pete' Walsh",
    author_email="ronnie@structurely.com, epwalsh@structurely.com",
    url="https://github.com/structurely/csa",
    packages=["pycsa"],
    package_dir={"pycsa": "csa"},
    keywords=[
        "csa",
        "sa",
        "simulated annealing",
        "annealing",
        "coupled simulated annealing",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering",
    ],
)
