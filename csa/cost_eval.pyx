from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
cimport numpy as np


DTYPE = np.float
ctypedef np.float_t DTYPE_t

PI = np.pi
UPPER_BOUNDBOX = 2 * PI
LOWER_BOUNDBOX = 0


def csa_eval_cost(np.ndarray solution, int dimension, int functionNumber):
    """
    Evaluate the current cost function.
    """
    cdef DTYPE_t e
    if functionNumber == 1998:
        e = 0
        for i in range(dimension):
            e += solution[i]
    #  elif functionNumber == 1999:
        #  e = 0
        #  for i in range(dimension - 1):
            #  xx = solution[i]
            #  yx = solution[i + 1]  # check if correct
            #  e = sin(math.sqrt(xx ** 2 + yx ** 2)) / math.sqrt(xx ** 2 + yx ** 2)
    elif functionNumber == 2000:  # sin(0)+cos(1)+sin(2)+cos(3)+..
        e = 0
        for i in range(dimension):
            if (i % 2 == 0):
                e += np.sin(PI * solution[i])
            else:
                e += np.cos(PI * solution[i])

    elif functionNumber == 2001:  # Sphere function
        solutionScale = 10
        e = 0
        for i in range(dimension):
            e += (solutionScale * solution[i]) ** 2

    elif functionNumber == 2002:  # Rosenbrock's function
        solutionScale = 2.048
        e = 0
        for i in range(dimension - 1):
            e += 100 * (solutionScale * solution[i + 1] - (solutionScale * solution[i])) ** 2 + (1 - solutionScale * solution[i]) ** 2

    elif functionNumber == 2003:  # Ackey's function
        solutionScale = 32.768
        tmpvar1 = 0
        for i in range(dimension):
            tmpvar1 += (solutionScale * solution[i]) ** 2
        tmpvar2 = 0
        for i in range(dimension):
            tmpvar2 += np.cos(2.0 * PI * solutionScale * solution[i])
        e = -20 * np.exp(-0.2 * np.sqrt(tmpvar1 / dimension)) - np.exp(tmpvar2 / dimension) + 20 + np.exp(1)


    elif functionNumber == 2004:  # Griewanks' function
        solutionScale = 600
        tmpvar1 = 0
        for i in range(dimension):
            tmpvar1 += (solutionScale * solution[i]) ** 2
        tmpvar2 = 1
        for i in range(dimension):
            tmpvar2 *= np.cos(solutionScale * solution[i] / np.sqrt(i + 1))
        e = tmpvar1 / 4000 - tmpvar2 + 1


    elif functionNumber == 2005:  # Weiersstrass function
        solutionScale = 0.5
        a = 0.5
        b = 3
        kmax = 20
        e = 0
        for i in range(dimension):
            tmpvar1 = 0
            for k in range(kmax + 1):
                tmpvar1 += (a ** k) * np.cos(2.0 * PI * (b ** k) * (solutionScale * solution[i] + 0.5))
            e += tmpvar1
        tmpvar1 = 0
        for k in range(kmax + 1):
            tmpvar1 += (a ** k) * np.cos(2 * PI * (b ** k) * 0.5)
        e -= (dimension) * tmpvar1


    elif functionNumber == 2006:  # Rastrin's function
        solutionScale = 5.12
        e = 0
        for i in range(dimension):
            e += (solutionScale * solution[i]) ** 2 - 10 * np.cos(2 * PI * solutionScale * solution[i]) + 10

    elif functionNumber == 2007:  # Noncontinuous Rastrin's function
        solutionScale = 5.12
        e = 0
        for i in range(dimension):
            y = (solutionScale * solution[i] if np.abs(solutionScale * solution[i]) < 0.5 else round(2 * solutionScale * solution[i]) / 2)

    elif functionNumber == 2008:  # Schwefel's function
        solutionScale = 500
        tmpvar1 = 0
        for i in range(dimension):
            tmpvar1 += solutionScale * solution[i] * np.sin(np.sqrt(np.abs(solutionScale * solution[i])))
        e = - tmpvar1 + 419 * dimension

    elif functionNumber == 2015:
        solutionScale = 500

    elif functionNumber == 2016:
        solutionScale = 500

    # Functions from the paper: Sample-sort simulated annenaling, in IEEE TSMC-B
    elif functionNumber == 3001: # Function Branin
        x1 = 10 * solution[0] + 5;
        x2 = 7.5 * solution[1] + 7.5
        e = (x2-(5.1/(4*PI*PI))*x1*x1+(5/PI)*x1-6) ** 2 + 10*(1-(1/(8*PI))) * np.cos(x1)+10

    elif functionNumber == 3002: # Function GoldPrice
        x1 = 2 * solution[0]
        x2 = 2 * solution[1]
        e = (1.0 + (x1+x2+1.0) ** 2 * (19.0 - 14.0*x1 + 3.0*x1*x1 -14.0*x2 + 6.0*x1*x2 +3.0*x2*x2)) * (30.0+(2.0*x1-3.0*x2) ** 2) \
            * (18.0 -32.0*x1 +12.0*x1*x1 +48.0*x2 -36.0*x1*x2 +27.0*x2*x2)

    elif functionNumber == 3008: # Function Griewank2
        solutionScale = 100
        tmpvar1 = 0
        for i in range(2):
            tmpvar1 += (solutionScale*solution[i]) ** 2
        tmpvar2 = 1
        for i in range(2):
            tmpvar2 *= np.cos(solutionScale*solution[i]/np.sqrt(i+1))
        e = tmpvar1/200 - tmpvar2 +1;

    elif functionNumber == 4000: # Multiobjective function example
        cost1 = csa_eval_cost(solution, dimension-2,2001)
        for i in range(dimension-2):
            solution[i] += 0.5
        cost2 = csa_eval_cost(solution, dimension-2,2007)
        for i in range(dimension-2):
            solution[i] -= 0.5
        par1 = np.abs(solution[dimension-1])
        par2 = np.abs(solution[dimension])
        parNorm = par1 + par2
        par1 /= parNorm
        par2 /= parNorm
        e =  par1*cost1 + par2*cost2

    elif functionNumber == 4001: # Multiobjective function SCH from NSGA-II
        solutionScale = 1000
        cost1 = (solutionScale*solution[0]) ** 2
        cost2 = (solutionScale*solution[0]-2) ** 2
        par1 = np.abs(solution[dimension-1])
        par2 = np.abs(solution[dimension])
        parNorm = par1 + par2
        par1 /= parNorm
        par2 /= parNorm
        e =  par1*cost1 + par2*cost2

    elif functionNumber == 4002: # Multiobjective function FON  from NSGA-II
        solutionScale = 4
        cost1 = cost2 = 0
        for i in range(3):
            cost1 += (solutionScale*solution[i]-(1/np.sqrt(3))) ** 2
            cost2 += (solutionScale*solution[i]+(1/np.sqrt(3))) ** 2
        cost1 = 1.0 - np.exp(-cost1);
        cost2 = 1.0 - np.exp(-cost2);
        par1 = np.abs(solution[dimension-1]);
        par2 = np.abs(solution[dimension]);
        parNorm = par1 + par2
        par1 /= parNorm
        par2 /= parNorm
        e =  par1*cost1 + par2*cost2

    else:
        e = np.inf

    return e
