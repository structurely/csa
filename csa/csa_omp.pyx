from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from cython cimport parallel
from libc.stdlib cimport abort, malloc, free
cimport openmp
import random
import math

PI = 3.14159265358979323846264338327

cdef int MAXITER = 1000000
cdef double TGEN = 0.01
cdef int DIMENSION = 10

cdef struct SharedCacheLine:
    double cost
    char padding[56]

cdef struct SharedBestCosts:
    double cost
    char padding[56]

cdef struct drand48_data
ctypedef openmp.omp_lock_t lock_t


def main(int numOptimizers, int numFunctions):
    cdef int maxIter = MAXITER
    cdef int dim = DIMENSION
    cdef double tgen = TGEN
    cdef double tac = 0.9
    cdef int gamma = 0

    cdef SharedCacheLine * sharedValues = <SharedCacheLine * > malloc(numOptimizers * sizeof(SharedCacheLine))
    cdef SharedBestCosts * sharedBestCost = <SharedBestCosts * > malloc(numOptimizers * sizeof(SharedBestCosts))
    cdef lock_t lock_tac
    openmp.omp_init_lock(& lock_tac)

    cdef int iter = 0
    cdef int k
    cdef int j
    cdef int optId = openmp.omp_get_thread_num()
    cdef double * curSol
    cdef double * temp
    cdef double * sol
    cdef double bestcost
    cdef double tmp
    cdef double prob
    cdef double probVar
    cdef double result = 0
    cdef double cost
    cdef double maxCost = 0
    # cdef drand48_data * buffer

    with nogil, parallel.parallel(num_threads=numOptimizers):
        curSol = <double * >malloc(dim * sizeof(double))
        Sol = <double * >malloc(dim * sizeof(double))

        with gil:
            for j in range(dim):
                result = random.getrandbits(48)
                curSol[j] = result * 2 - 1
            bestcost = 0
            maxCost = sharedValues[0].cost
            for k in range(1, numOptimizers):
                if (sharedValues[k].cost > maxCost):
                    maxCost = sharedValues[k].cost
