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

    elif functionNumber == 2004: # Griewanks' function
        # TODO
        pass
    elif functionNumber == 2005:
        # TODO
        pass
    elif functionNumber == 2006:
        # TODO
        pass
    elif functionNumber == 2007:
        # TODO
        pass
    elif functionNumber == 2008:
        # TODO
        pass
    elif functionNumber == 2015:
        # TODO
        pass
    elif functionNumber == 2016:
        # TODO
        pass
    elif functionNumber == 3001:
        # TODO
        pass
    elif functionNumber == 3002:
        # TODO
        pass
    elif functionNumber == 3008:
        # TODO
        pass
    elif functionNumber == 4000:
        # TODO
        pass
    elif functionNumber == 4001:
        # TODO
        pass
    elif functionNumber == 4002:
        # TODO
        pass
    else:
        e = math.inf
    return e
