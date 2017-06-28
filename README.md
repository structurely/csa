# Coupled simulated annealing

The original paper describing Coupled Simulated Annealing (CSA) can be found here:

ftp://ftp.esat.kuleuven.be/sista/sdesouza/papers/CSA2009accepted.pdf

Essentially, CSA is like multiple simulated annealing (i.e. `m` independent SA processes run in parallel),
except that the acceptance probability at each step is calculated as a function of the current state
across *all* `m` processes. For a more complete description of the general CSA algorithm, see 
[Description of CSA](#description-of-csa) below.

## Installation

Using `pip`:

```
pip install pycsa
```

Directly from `GitHub`:

```
pip install -e git+https://github.com/structurely/csa.git
```

## Usage

See [examples/travelling_salesman.ipynb](https://github.com/structurely/csa/blob/master/examples/travelling_salesman.ipynb) for an example of CSA applied to the [travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (TSP).

## Contributing

Feel free to submit pull requests and issues.

## License

See [LICENSE.txt](https://github.com/structurely/csa/blob/master/LICENSE.txt).

## Related

- [perrygeo/simanneal](https://github.com/perrygeo/simanneal): a Python implementation of (single) simulated 
annealing.
- [docs.scipy.org](https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.anneal.html):
the SciPy implementation of simulated annealing.

## Description of CSA

Suppose we are trying optimize (meaning minimize, in this case) some function 
`my_function()` which takes `x` as input
and outputs a float.

We are going to run `m` processes in parallel. Therefore `x_i` will denote the current solution
for the `m`th process.

### Definitions

Before describing the algorithm, we will need to define the following functions and parameters:

- `energy_func(tac, ...)` is a function which takes `tac` (the acceptance "temperature") and the quantities 
`my_function(x_1), ..., my_function(x_m)` as input and outputs a float.
That is, `energy_func` represents the "energy" of the current solution set `x_1, ..., x_m`.
- `generation_schedule(tgen, iteration)` is a function which takes `tgen` (the generation "temperature") and the 
number of 
the current iteration as input. The `generation_schedule` function determines how much `tgen` is
decreased at each iteration. A typical choice for `generation_schedule` is just to multiply the current value 
of `tgen` by 0.9999.
- `default_tgen` is the initial value given to `tgen`.
- `acceptance_schedule(tac, iteration)` is a function which takes `tac` (the acceptance "temperature") and the number
of the current iteration as input. This function determines how much `tac` will be decreased at each
iteration. A typical choice for `acceptance_schedule` is just to multiply `tac` by 0.99.
- `default_tac` is the initial value given to `tac`.
- `random_probe(i, tgen)` is a function which produces a random value for each `x_i` according to
some distribution which depends on `tgen`.
- `acceptance_prob(tac, current_state, x_i, y_i)` is a function that outputs a number between 0 
and 1.
- `n` the number of inner iterations (how many times we repeat steps 2 and 3 over each overall iteration).
- `N` the number of outer iterations.

> NOTE: The choices for `energy_func()`, `generation_schedule()`, `acceptance_schedule()`,
and `random_probe()` are what distinguish the particular classes of CSA algorithms.

### The algorithm

1. **Initialization** 
  - Assign random initial solutions to `x_1`, ..., `x_m`.
  - Let `gamma = energy_func(my_function(x_1), ..., my_function(x_m))`.
  - Set `tgen = default_tgen`.
  - Set `tac = default_tac`.
  - Set the inner iteration index `j = 0`.
  - Set the outer iteration index `k = 0`.

2. **Generation**
  - For each `i in (1, ..., m)`:
    - Generate a "probing" solution `y_i = x_i + e`, where `e` is randomly generated
	from the function `random_probe(i, tgen)`.

3. **Acceptance**
  - For each `i in (1, ..., m)`:
    - If `my_function(y_i) < my_function(x_i)`, set `x_i = y_i`.
	- Else, set `p = acceptance_prob(gamma, x_i, y_i)`. Then sample `r` from a uniform(0, 1) distribution
	and set `x_i = y_i` if `r < p`, otherwise keep `x_i = x_i`.
  - Now update `gamma = energy_func(my_function(x_1), ..., my_function(x_m))`.
  - Increment `j += 1`.
  - If `j < n`, go back to step 2, otherwise set `j = 0` and continue to step 4.

4. **Cooling**
  - Decrease the "temperatures" `tgen` and `tac` according to their respective schedules,  i.e. we set `tgen = generation_schedule(tgen, k)` and 
  `tac = acceptance_schedule(tac, k)`.
  - Increment `k += 1`.

5. **Stop**
  - Stop if the stopping criteria is met or if `k >= N`. Otherwise return to step 2.
