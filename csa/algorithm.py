from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import multiprocessing as mp
import random

try:
    xrange
except NameError:
    xrange = range


class CoupledAnnealer(object):

    def __init__(self, target_function, probe_function,
                 initial_state=None,
                 initial_states=[],
                 steps=100000,
                 update_interval=5,
                 tgen_initial=0.01,
                 tgen_schedule=0.99999,
                 tacc_initial=0.9, 
                 tacc_schedule=0.99,
                 desired_variance=None,
                 n_probes=10, 
                 processes=-1):
        self.target_function = target_function
        self.probe_function = probe_function
        self.initial_state = initial_state
        self.initial_states = initial_states
        self.n_probes = n_probes
        self.processes = processes if processes > 0 else mp.cpu_count()
        self.update_interval = update_interval
        self.tgen = tgen_initial
        self.tacc = tacc_initial
        self.tgen_schedule = tgen_schedule
        self.tacc_schedule = tacc_schedule
        
        # Set desired_variance.
        if desired_variance is None:
            desired_variance = 0.99 * (n_probes - 1) / (n_probes ** 2)
        self.desired_variance = desired_variance

        # Initialize state.
        if initial_state is None:
            assert len(initial_states) == self.n_probes
            self.probe_states = initial_states
        else:
            self.probe_states = [initial_state] * n_probes

        # Shallow copy.
        self.current_states = self.probe_states[:]

        # Initialize energies.
        self.probe_energies = self.current_energies = [None] * n_probes

        # Set up mp queue.
        manager = mp.Manager()
        self.queue = manager.Queue()

    def worker_probe(self, i):
        state = self.current_states[i]
        probe = self.probe_function(state)
        energy = self.target_function(probe)
        self.queue.put((i, energy, probe))

    def listener(self):
        while True:
            res = self.queue.get()
            if res == '__kill__':
                break
            i, energy, probe = res
            self.probe_energies[i] = energy
            self.probe_states[i] = probe

    def update_state(self):
        # Set up the mp pool.
        pool = mp.Pool(processes=self.processes)

        # Put the listener to work first.
        watcher = pool.apply_async(listener, args=())

        # Now put the workers to work.
        jobs = []
        for i in xrange(self.n_probes):
            job = pool.apply_async(self.worker_probe, args=(i,))
            jobs.append(job)

        # Collect the results from the current iteration through the pool queue.
        for job in jobs:
            job.get()

        # Done. Kill the listener.
        queue.put('__kill__')
        pool.close()

    def step(self, k):
        cool = True if k % self.update_interval == 0 else False

        max_energy = max(self.current_energies)
        exp_terms = []

        if cool:
            exp_terms2 = []

        for i in xrange(self.n_probes):
            E = self.current_energies[i]
            exp_terms.append(math.exp((E - max_energy) / self.tacc))
            # No need to calculate this if we are not cooling this step.
            if cool:
                exp_terms2.append(math.exp(2.0 * (E - max_energy) / self.tacc))

        gamma = sum(exp_terms)
        prob_accept = [x / gamma for x in exp_terms]

        # Determine whether to accept or reject probe.
        for i in xrange(self.n_probes):
            state_energy = self.current_energies[i]
            probe_energy = self.probe_energies[i]
            probe = self.probe_states[i]
            p = prob_accept[i]
            if (probe_energy < state_energy) or (random.uniform(0, 1) < p):
                self.current_energies[i] = probe_energy
                self.current_states[i] = probe

        # Update temperatures according to schedule.
        if cool:
            # Update generation temp.
            self.tgen = self.tgen * self.tgen_schedule
            # Update acceptance temp.
            sigma2 = (self.n_probe * sum(exp_terms2) / (gamma ** 2) - 1) 
            sigma2 = sigma2 / (self.n_probes ** 2)
            if sigma < self.desired_variance:
                self.tacc *= self.tacc_schedule
            else:
                self.tacc *= (2 - self.tacc_schedule)

    def anneal(self):
        for k in xrange(1, self.steps + 1):
            self.update_state()
            self.step(k)
