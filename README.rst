Coupled simulated annealing
===========================

|Build Status|
|PyPI|

Coupled simulated annealing (CSA) is a generalization of simulated annealing (SA),
which is an optimization algorithm that doesn't use any information about the derivates
of a function. The original paper describing CSA can be
found here:

ftp://ftp.esat.kuleuven.be/sista/sdesouza/papers/CSA2009accepted.pdf

Essentially, CSA is like multiple simulated annealing (i.e. ``m``
independent SA processes run in parallel), except that the acceptance
probability at each step is calculated as a function of the current
state across *all* ``m`` processes. For a more complete description of
the general CSA algorithm, see 
`Description of CSA <https://docs.structurely.com/pycsa/v0.1.2/#description-of-csa>`__.

Installation
------------

Using ``pip``:

::

    pip install pycsa

Directly from ``GitHub``:

::

    pip install git+https://github.com/structurely/csa.git

Usage
-----

See
`examples/travelling\_salesman.ipynb <https://github.com/structurely/csa/blob/dev/examples/travelling_salesman.ipynb>`__
for an example of CSA applied to the `travelling salesman problem
(TSP) <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`__.

Contributing
------------

Feel free to submit pull requests and issues.

License
-------

See
`LICENSE.txt <https://github.com/structurely/csa/blob/dev/LICENSE.txt>`__.

Related
-------

-  `perrygeo/simanneal <https://github.com/perrygeo/simanneal>`__: a
   Python implementation of (single) simulated annealing.
-  `docs.scipy.org <https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.anneal.html>`__:
   the SciPy implementation of simulated annealing.

.. |Build Status| image:: https://travis-ci.org/structurely/csa.svg?branch=dev
   :target: https://travis-ci.org/structurely/csa

.. |PyPI| image:: https://badge.fury.io/py/pycsa.svg
    :target: https://badge.fury.io/py/pycsa
