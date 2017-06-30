Description of CSA
------------------

Suppose we are trying optimize (meaning minimize, in this case) some
function :math:`E` which takes :math:`x` as input and outputs a
real number.

We are going to run :math:`m` processes in parallel. Therefore :math:`x_i` will
denote the current solution for the :math:`m`\ th process.

Definitions
~~~~~~~~~~~

Before describing the algorithm, we will need to define the following
functions and parameters:

-  :math:`\gamma \equiv \gamma(T_{acc}, f(x_1), ..., f(x_m))` is a function which 
   takes :math:`T_{acc}` (the acceptance "temperature") and the quantities
   :math:`f(x_1), ..., f(x_m)` as input and outputs a
   real number. In some sense, :math:`\gamma` represents the "energy" of the
   current solution set :math:`x_1, ..., x_m`.
-  :math:`U(T_{gen}, k)` is a function which takes
   :math:`T_{gen}` (the generation "temperature") and the number of the current
   iteration :math:`k` as input. The generation schedule function :math:`U` determines
   how much :math:`T_{gen}` is decreased at each iteration. A typical choice
   for :math:`U` is :math:`U(T_{gen}, k) := 0.9999 T_{gen}`.
-  :math:`T_{gen}^{(0)}` is the initial value given to :math:`T_{gen}`.
-  :math:`V(T_{acc}, k)` is a function which takes
   :math:`T_{acc}` and the number of the current
   iteration :math:`k` as input. This function determines how much :math:`T_{acc}` will be
   decreased (or sometimes increased) at each iteration. 
-  :math:`T_{acc}^{(0)}` is the initial value given to :math:`T_{acc}`.
-  :math:`g(\epsilon, T_{gen})` is a probability distribution function for :math:`\epsilon`
   which depends on :math:`T_{gen}`.
-  :math:`A(T_{acc}, \gamma, x_i, y_i)` is a function that
   outputs a number between 0 and 1, which represents the acceptance probability.
-  :math:`n` is the number of inner iterations (how many times we repeat steps
   2 and 3 over each overall iteration).
-  :math:`N` is the number of outer iterations.

    NOTE: The choices for :math:`\gamma`, :math:`U`,
    :math:`V`, and :math:`g` are what
    distinguish the particular classes of CSA algorithms.

The algorithm
~~~~~~~~~~~~~

1. **Initialization**

-  Assign random initial solutions to :math:`x_1`, ..., :math:`x_m`.
-  Let :math:`\gamma_0 = \gamma(f(x_1), ..., f(x_m))`.
-  Set the inner iteration index :math:`j = 0`.
-  Set the outer iteration index :math:`k = 0`.

2. **Generation**

-  For each :math:`i \in \{1, ..., m\}`:

   -  Generate a "probing" solution :math:`y_i := x_i + \epsilon`, where 
      :math:`\epsilon` is randomly generated from the distribution
      :math:`g(\epsilon, T_{gen}^{(0)})`.

3. **Acceptance**

-  For each :math:`i \in \{1, ..., m\}`:

   -  If :math:`f(y_i) < f(x_i)`, set :math:`x_i := y_i`.
   -  Else, set :math:`\alpha := A(T_{acc}^{(k)}, \gamma, x_i, y_i)`. Then sample
      :math:`r` from a uniform(0, 1) distribution and set :math:`x_i := y_i` if
      :math:`r < p`, otherwise keep :math:`x_i` as it is.

-  Now update
   :math:`\gamma_k := \gamma(f(x_1), ..., f(x_m))`.
-  Increment :math:`j` by 1.
-  If :math:`j < n`, go back to step 2, otherwise set :math:`j = 0` and continue
   to step 4.

4. **Cooling**

-  Decrease the generation and acceptance "temperatures" 
   for the next iterations according to their respective schedules, i.e. set
   :math:`T_{gen}^{(k+1)} = U(T_{gen}^{(k)}, k)` and
   :math:`T_{acc}^{(k+1)} = V(T_{acc}^{(k)}, k)`.
-  Increment :math:`k` by 1.

5. **Stop**

-  Stop if the stopping criteria is met or if :math:`k >= N`. Otherwise
   return to step 2.

.. |Build Status| image:: https://travis-ci.org/structurely/csa.svg?branch=dev
   :target: https://travis-ci.org/structurely/csa

.. |PyPI| image:: https://badge.fury.io/py/pycsa.svg
    :target: https://badge.fury.io/py/pycsa
