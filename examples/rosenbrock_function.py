#!/usr/bin/env python
# =============================================================================
# File Name:     rosenbrock_function.py
# Orig Author:   Evan Pete Walsh
# Contact:       epwalsh@structurely.com
# Creation Date: 2017-06-28
# Last Modified: 2017-06-28 16:33:50
# =============================================================================

"""
Example of CSA applied to the Rosenbrock function.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random
from pycsa import CoupledAnnealer

try:
    xrange
except NameError:
    xrange = range


SOLUTION_SCALE = 2.048
DIMENSION      = 2
N_ANNEALERS    = 10
STEPS          = 100


def rosenbrock(solution):
    e = 0
    for i in xrange(len(solution) - 1):
        e += (SOLUTION_SCALE * solution[i + 1] - (SOLUTION_SCALE * solution[i])) ** 2 
        e += (1 - SOLUTION_SCALE * solution[i]) ** 2
        e *= 100
    return e


def probe(solution, tgen):
    sigma = 100 * tgen
    probe_solution = []
    for x in solution:
        probe_solution.append(x + random.normalvariate(0, sigma))
    return probe_solution


initial_state = [tuple((random.normalvariate(0, 5) for _ in xrange(DIMENSION)))
                 for x in xrange(N_ANNEALERS)]

annealer = CoupledAnnealer(
    rosenbrock,
    probe,
    initial_state=initial_state,
    steps=STEPS,
    processes=4,
    verbose=1,
)

annealer.anneal()
energy, state = annealer.get_best()

x = ', '.join(["{:,.5f}".format(x) for x in state])
print("Energy: {:,.5f}, Position: ({})".format(energy, x))
