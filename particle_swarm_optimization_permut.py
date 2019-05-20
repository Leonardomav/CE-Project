# ------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   Simple Particle Swarm Optimization (PSO) with Python
#   July, 2016
#
# ------------------------------------------------------------------------------+

# --- IMPORT DEPENDENCIES ------------------------------------------------------+

import random
import math
from timeit import default_timer as timer

# --- MAIN ---------------------------------------------------------------------+


class Particle:
    def __init__(self, dicio):
        cities = [x for x in dicio.keys()]
        random.shuffle(cities)
        self.position_indiv = cities        # particle position
        self.pos_best_indiv = []          # best position individual
        self.err_best_indiv = -1          # best error individual
        self.err_indiv = -1               # error individual
        self.personal_section = 0
        self.cognitive_section = 0
        self.social_section = 0

    # evaluate current fitness
    def evaluate(self, costFunc, dicio):
        self.err_indiv = costFunc(self.position_indiv, dicio)

        # check to see if the current position is an individual best
        if self.err_indiv < self.err_best_indiv or self.err_best_indiv == -1:
            self.pos_best_indiv = self.position_indiv
            self.err_best_indiv = self.err_indiv

    # update new particle velocity
    def update_velocity(self, err_best_local, weight=0.5,
                        cognitive_param=1, social_param=2):
        r1 = random.random()
        r2 = random.random()

        vel_personal = weight * \
            (1 / self.err_indiv) if self.err_indiv > 0 else 0
        vel_cognitive = cognitive_param * r1 * \
            (1 / self.err_best_indiv) if self.err_best_indiv > 0 else 0
        vel_social = social_param * r2 * \
            (1 / err_best_local) if err_best_local > 0 else 0

        total_velocity = vel_cognitive + vel_social + vel_personal

        self.personal_section = math.floor(
            len(self.position_indiv) * (vel_personal / total_velocity))
        if vel_cognitive > 0:
            self.cognitive_section = math.floor(
                len(self.position_indiv) * (vel_cognitive / total_velocity))
        if vel_social > 0:
            self.social_section = math.floor(
                len(self.position_indiv) * (vel_social / total_velocity))

    # update the particle position based off new velocity updates
    def update_position(self, pos_best_local):
        personal_start_index = random.randint(
            0, len(self.pos_best_indiv) - self.personal_section)
        cognitive_start_index = random.randint(
            0, len(self.pos_best_indiv) - self.cognitive_section)
        social_start_index = random.randint(
            0, len(self.pos_best_indiv) - self.social_section)

        availability_mask = [True for _ in range(len(self.pos_best_indiv))]
        personal_mask = [True if personal_start_index < x < personal_start_index +
                         self.personal_section else False for x in range(len(self.pos_best_indiv))]
        cognitive_mask = [True if cognitive_start_index < x < cognitive_start_index +
                          self.cognitive_section else False for x in range(len(self.pos_best_indiv))]
        social_mask = [True if social_start_index < x < social_start_index +
                       self.social_section else False for x in range(len(self.pos_best_indiv))]

        new_position = []

        aux_mask = []
        for x, y, index in zip(
                availability_mask, personal_mask, range(len(personal_mask))):
            if x and y:
                new_position.append(index)
                aux_mask.append(True)
            else:
                aux_mask.append(False)
        availability_mask = [
            x ^ y for x, y in zip(
                availability_mask, aux_mask)]

        aux_mask = []
        for x, y, index in zip(
                availability_mask, cognitive_mask, range(len(cognitive_mask))):
            if x and y:
                new_position.append(index)
                aux_mask.append(True)
            else:
                aux_mask.append(False)
        availability_mask = [
            x ^ y for x, y in zip(
                availability_mask, aux_mask)]

        aux_mask = []
        for x, y, index in zip(
                availability_mask, social_mask, range(len(social_mask))):
            if x and y:
                new_position.append(index)
                aux_mask.append(True)
            else:
                aux_mask.append(False)
        availability_mask = [
            x ^ y for x, y in zip(
                availability_mask, aux_mask)]

        for x in self.position_indiv:
            if availability_mask[x]:
                new_position.append(x)

        self.position_indiv = new_position


class ParticleSwarm():
    def __init__(self, costFunc, x0, dicio, num_particles,
                 maxiter, weight, cognitive_param, social_param):
        global num_dimensions

        num_dimensions = len(x0)
        err_best_g = -1                   # best error for group
        pos_best_g = []                   # best position for group
        self.best_individuals = []
        self.fitness_averages = []
        self.population_initialization_time = 0.0
        self.generation_calculation_times = []

        # establish the swarm
        swarm = []
        start = timer()
        for i in range(num_particles):
            swarm.append(Particle(dicio))
        end = timer()
        self.population_initialization_time = end - start

        # begin optimization loop
        i = 0
        while i < maxiter:
            # print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            average_fitness = 0.0
            self.generation_calculation_times.append(0)
            for j in range(num_particles):
                print(i, "/", maxiter, " ", j, "/", num_particles)
                t1_start = timer()
                swarm[j].evaluate(costFunc, dicio)
                t1_end = timer()
                t1 = t1_end - t1_start
                self.generation_calculation_times[-1] += t1
                average_fitness += swarm[j].err_indiv

                # determine if current particle is the best (globally)
                if swarm[j].err_indiv < err_best_g or err_best_g == -1:
                    pos_best_g = list(swarm[j].position_indiv)
                    err_best_g = float(swarm[j].err_indiv)

            # cycle through swarm and update velocities and position
            for j in range(num_particles):
                t2_start = timer()
                swarm[j].update_velocity(
                    err_best_g, weight, cognitive_param, social_param)
                swarm[j].update_position(pos_best_g)
                t2_end = timer()
                t2 = t2_end - t2_start
                self.generation_calculation_times[-1] += t2
            i += 1

            average_fitness = average_fitness / num_particles
            self.fitness_averages.append(average_fitness)
            self.best_individuals.append((pos_best_g, err_best_g))

        # print final results
        print('FINAL:')
        print(pos_best_g)
        print(err_best_g)
