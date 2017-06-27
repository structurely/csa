from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from cython.parallel cimport parallel
from libc.stdlib cimport abort, malloc, free
cimport openmp

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
    openmp.omp_init_lock( & lock_tac)
