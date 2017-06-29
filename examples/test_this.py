#!/usr/bin/env python
# =============================================================================
# File Name:     test_this.py
# Orig Author:   Evan Pete Walsh
# Contact:       epwalsh@structurely.com
# Creation Date: 2017-06-27
# Last Modified: 2017-06-27 18:50:06
# =============================================================================

"""
docstring
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys; sys.path.append('..')
import math
import random
import time

from csa.algorithm import CoupledAnnealer


try:
    xrange
except NameError:
    xrange = range


# latitude and longitude for the twenty largest U.S. cities
cities = {
    'New York City': (40.72, 74.00),
    'Los Angeles': (34.05, 118.25),
    'Chicago': (41.88, 87.63),
    'Houston': (29.77, 95.38),
    'Phoenix': (33.45, 112.07),
    'Philadelphia': (39.95, 75.17),
    'San Antonio': (29.53, 98.47),
    'Dallas': (32.78, 96.80),
    'San Diego': (32.78, 117.15),
    'San Jose': (37.30, 121.87),
    'Detroit': (42.33, 83.05),
    'San Francisco': (37.78, 122.42),
    'Jacksonville': (30.32, 81.70),
    'Indianapolis': (39.78, 86.15),
    'Austin': (30.27, 97.77),
    'Columbus': (39.98, 82.98),
    'Fort Worth': (32.75, 97.33),
    'Charlotte': (35.23, 80.85),
    'Memphis': (35.12, 89.97),
    'Baltimore': (39.28, 76.62)
}

# initial state, a randomly-ordered itinerary
init_state = list(cities.keys())
random.shuffle(init_state)

def distance(a, b):
    """Calculates distance between two latitude-longitude coordinates."""
    R = 3963  # radius of Earth (miles)
    lat1, lon1 = math.radians(a[0]), math.radians(a[1])
    lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * R


# create a distance matrix
distance_matrix = {}
for ka, va in cities.items():
    distance_matrix[ka] = {}
    for kb, vb in cities.items():
        if kb == ka:
            distance_matrix[ka][kb] = 0.0
        else:
            distance_matrix[ka][kb] = distance(va, vb)


def probe(positions):
    """
    Swap two cities in the route.
    """
    a = random.randint(0, len(positions) - 1)
    b = random.randint(0, len(positions) - 1)
    positions[a], positions[b] = positions[b], positions[a]
    return positions


def target(positions):
    """
    Calculates the length of the route.
    """
    e = 0
    for i in xrange(len(positions)):
        e += distance_matrix[positions[i-1]][positions[i]]
    return e

start_time = time.time()
annealer = CoupledAnnealer(target, probe, 
                           initial_state=init_state,
                           steps=100)
annealer.anneal()

energies = annealer.current_energies
states = annealer.current_states
best = energies.index(min(energies))
state = states[best]
energy = energies[best]

while state[0] != 'New York City':
    state = state[1:] + state[:1]

print("%i mile route:" % energy)
for city in state:
    print("\t", city)
    
print("time of execution: ",time.time()-start_time)
