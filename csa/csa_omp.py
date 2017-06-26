from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math

PI = 3.14159265358979323846264338327
UPPER_BOUNDBOX = 2 * PI
LOWER_BOUNDBOX = 0


def CSA_EvalCost(solution, dimension, functionNumber):
    xx = 0
    yx = 0
    if functionNumber == 1998:
        e = 0
        for i in range(dimension):
            e += solution[i]
        break
    elif functionNumber == 1999:
        e = 0
        for i in range(dimension - 1):
            xx = solution[i]
            yx = solution[i + 1]  # check if correct
            e = math.sin(math.sqrt(xx ** 2 + yx ** 2)) / math.sqrt(xx ** 2 + yx ** 2)
        break
    elif functionNumber == 2000:  # sin(0)+cos(1)+sin(2)+cos(3)+..
        e = 0
        for i in range(dimension):
            if (i % 2 == 0):
                e += math.sin(PI * solution[i])
            else:
                e += math.cos(PI * solution[i])
        break
    elif functionNumber == 2001:  # Sphere function
        solutionScale = 10
        e = 0
        for i in range(dimension):
            e += (solutionScale * solution[i]) ** 2
        break
    elif functionNumber == 2002:  # Rosenbrock's function
        solutionScale = 2.048
        e = 0
        for i in range(dimension - 1):
            e += 100 * math.pow(solutionScale * solution[i + 1] - math.pow(solutionScale * solution[i], 2), 2) + math.pow(1 - solutionScale * solution[i], 2)
        break
    elif functionNumber == 2003:  # Ackey's function
        solutionScale = 32.768
        tmpvar1 = 0
        for i in range(dimension):
            tmpvar1 += math.pow(solutionScale * solution[i], 2)
        tmpvar2 = 0
        for i in range(dimension):
            tmpvar2 += math.cos(2.0 * PI * solutionScale * solution[i])
        e = -20 * math.exp(-0.2 * math.sqrt(tmpvar1 / dimension)) - math.exp(tmpvar2 / dimension) + 20 + math.exp(1)
        break

    elif functionNumber == 2004:  # Griewanks' function
        solutionScale = 600
        tmpvar1 = 0
        for i in range(dimension):
            tmpvar1 += math.pow(solutionScale * solution[i], 2)
        tmpvar2 = 1
        for i in range(dimension):
            tmpvar2 *= math.cos(solutionScale * solution[i] / sqrt(i + 1))
        e = tmpvar1 / 4000 - tmpvar2 + 1
        break

    elif functionNumber == 2005:  # Weiersstrass function
        solutionScale = 0.5
        a = 0.5
        b = 3
        kmax = 20
        e = 0
        for i in range(dimension):
            tmpvar1 = 0
            for k in range(kmax + 1):
                tmpvar1 += math.pow(a, k) * math.cos(2.0 * PI * math.pow(b, k) * (solutionScale * solution[i] + 0.5))
            e += tmpvar1
        tmpvar1 = 0
        for k in range(kmax + 1):
            tmpvar1 += math.pow(a, k) * math.cos(2 * PI * pow(b, k) * 0.5)
        e -= (dimension) * tmpvar1
        break

    elif functionNumber == 2006:  # Rastrin's function
        solutionScale = 5.12
        e = 0
        for i in range(dimension):
            e += math.pow(solutionScale * solution[i], 2) - 10 * math.cos(2 * PI * solutionScale * solution[i]) + 10
        break
    elif functionNumber == 2007:  # Noncontinuous Rastrin's function
        solutionScale = 5.12
        e = 0
        for i in range(dimension):
            y = (solutionScale * solution[i] if math.fabs(solutionScale * solution[i]) < 0.5 else round(2 * solutionScale * solution[i]) / 2)
        break
    elif functionNumber == 2008:  # Schwefel's function
        solutionScale = 500
        tmpvar1 = 0
        for i in range(dimension):
            tmpvar1 += solutionScale * solution[i] * math.sin(math.sqrt(math.fabs(solutionScale * solution[i])))
        e = - tmpvar1 + 419 * dimension
        break
    elif functionNumber == 2015:
        solutionScale = 500
        break
    elif functionNumber == 2016:
        solutionScale = 500
        break
    # Functions from the paper: Sample-sort simulated annenaling, in IEEE TSMC-B
    elif functionNumber == 3001: # Function Branin
        # TODO
        pass
    elif functionNumber == 3002: # Function GoldPrice
        # TODO
        pass
    elif functionNumber == 3008: # Function Griewank2
        # TODO
        pass
    elif functionNumber == 4000: # Multiobjective function example
        # TODO
        pass
    elif functionNumber == 4001: # Multiobjective function SCH from NSGA-II
        # TODO
        pass
    elif functionNumber == 4002: # Multiobjective function FON  from NSGA-II
        # TODO
        pass
    else:
        e = math.inf
    return e
