# Coupled simulated annealing

Suppose we are trying optimize (meaning minimize, in this case) some function 
`my_function()` which takes a vector of floats `x` as input
and outputs a float.

We are going to run `m` processes in parallel. Therefore `x_i` will denote the current solution
for the `m`th process.

Before describing the algorithm, we will need to define the following functions and parameters:

- `energy_func()` is a function which takes the vector `(my_function(x_1), ..., my_function(x_m))` as input
and outputs a float.
That is, `energy_func` represents the "energy" of the current solution set `x_1, ..., x_m`.
- `generation_schedule(generation_param, iteration)` is a function which takes `generation_param` and the 
number of 
the current iteration as input. The `generation_schedule` function determines how much `generation_param` is
decreased at each iteration.
- `default_generation_param` is the initial value given to `generation_param`.
- `acceptance_schedule(acceptance_param, iteration)` is a function which takes `acceptance_param` and the number
of the current iteration as input. This function determines how much `acceptance_param` will be decreased at each
iteration.
- `default_acceptance_param` is the initial value given to `acceptance_param`.
- `random_probe(i, generation_param)` is a function which produces a random value for each `x_i` according to
some distribution which depends on `generation_param`.
- `acceptance_prob(acceptance_param, current_state, x_i, y_i)` is a function that outputs a number between 0 
and 1.
- `n` the number of inner iterations (how many times we repeat steps 2 and 3 over each overall iteration).
- `N` the number of outer iterations.


The algorithm:

1. **Initialization** 
  - Assign random initial solutions to `x_1`, ..., `x_m`.
  - Let `current_state = energy_func(my_function(x_1), ..., my_function(x_m))`.
  - Set `generation_param = default_generation_param`.
  - Set `acceptance_param = default_acceptance_param`.
  - Set the inner iteration index `j = 0`.
  - Set the outer iteration index `k = 0`.

2. **Generation**
  - For each `i in (1, ..., m)`:
    - Generate a "probing" solution `y_i = x_i + e`, where `e` is randomly generated
	from the function `random_probe(i, generation_param)`.

3. **Acceptance**
  - For each `i in (1, ..., m)`:
    - If `my_function(y_i) < my_function(x_i)`, set `x_i = y_i`.
	- Else, set `p = acceptance_prob(current_state, x_i, y_i)`. Then sample `r` from a uniform(0, 1) distribution
	and set `x_i = y_i` if `r < p`, otherwise keep `x_i = x_i`.
  - Now update `current_state = energy_func(my_function(x_1), ..., my_function(x_m))`.
  - Increment `j += 1`.
  - If `j < n`, go back to step 2, otherwise set `j = 0` and continue to step 4.

4. **Cooling**
  - Decrease the "temperatures" `generation_param` and `acceptance_param` according to their respective schedules,  i.e. we set `generation_param = generation_schedule(generation_param, k)` and 
  `acceptance_param = acceptance_schedule(acceptance_param, k)`.
  - Increment `k += 1`.

5. **Stop**
  - Stop if the stopping criteria is met or if `k >= N`. Otherwise return to step 2.
