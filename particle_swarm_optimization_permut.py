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
import difflib
# --- MAIN ---------------------------------------------------------------------+

class Predator:
    def __init__(self, dicio):
        cities = [x for x in dicio.keys()]
        random.shuffle(cities)
        self.cities = cities
        self.position_indiv = cities        # particle position

    # update new particle velocity
    def update_velocity(self, weight=0.5,
                        cognitive_param=1, social_param=2):
        vel_social = random.random()
        vel_personal = 1 - vel_social 
        total_velocity = 1
        
        self.personal_section = math.floor(
            len(self.position_indiv) * (vel_personal / total_velocity))
        if vel_social > 0:
            self.social_section = math.floor(
                len(self.position_indiv) * (vel_social / total_velocity))

    # update the particle position based off new velocity updates
    def update_position(self, pos_best_local):
        personal_start_index = random.randint(
            0, len(self.position_indiv) - self.personal_section)
        social_start_index = random.randint(
            0, len(self.position_indiv) - self.social_section)

        availability_mask = [True for _ in range(len(self.position_indiv))]
        personal_mask = [True if personal_start_index < x < personal_start_index +
                         self.personal_section else False for x in range(len(self.position_indiv))]
        social_mask = [True if social_start_index < x < social_start_index +
                       self.social_section else False for x in range(len(self.position_indiv))]

        new_position = []
        aux_mask = []
        for x, y in zip(
                availability_mask, personal_mask):
            if x and y:
                aux_mask.append(True)
            else:
                aux_mask.append(False)
        for i in self.position_indiv:
            if aux_mask[i]:
                new_position.append(i)
        availability_mask = [
            x ^ y for x, y in zip(
                availability_mask, aux_mask)]

        aux_mask = []
        for x, y in zip(
                availability_mask, social_mask):
            if x and y:
                aux_mask.append(True)
            else:
                aux_mask.append(False)
        for i in pos_best_local:
            if aux_mask[i]:
                new_position.append(i)
        availability_mask = [
            x ^ y for x, y in zip(
                availability_mask, aux_mask)]
        
        random.shuffle(self.position_indiv)
        for x in self.position_indiv:
            if availability_mask[x]:
                new_position.append(x)
class Particle:
    def __init__(self, dicio):
        cities = [x for x in dicio.keys()]
        random.shuffle(cities)
        self.cities = cities
        self.position_indiv = cities        # particle position
        self.pos_best_indiv = []          # best position individual
        self.predator_position = []
        self.err_best_indiv = -1          # best error individual
        self.err_indiv = -1               # error individual
        self.personal_section = 0
        self.cognitive_section = 0
        self.social_section = 0
        self.fear_section = 0

    # evaluate current fitness
    def evaluate(self, costFunc, dicio):
        self.err_indiv = costFunc(self.position_indiv, dicio)

        # check to see if the current position is an individual best
        if self.err_indiv < self.err_best_indiv or self.err_best_indiv == -1:
            self.pos_best_indiv = self.position_indiv
            self.err_best_indiv = self.err_indiv

    # update new particle velocity
    def update_velocity(self, err_best_local, weight=0.5,
                        cognitive_param=1, social_param=2, fear_prob=0):
        r1 = random.random()
        r2 = random.random()
        r3 = random.random()
        
        vel_personal = weight * \
            (1 / self.err_indiv) if self.err_indiv > 0 else 0
        vel_cognitive = cognitive_param * r1 * \
            (1 / self.err_best_indiv) if self.err_best_indiv > 0 else 0
        vel_social = social_param * r2 * \
            (1 / err_best_local) if err_best_local > 0 else 0
        vel_fear = 0
        if random.random() < fear_prob:
            sm = difflib.SequenceMatcher(None, self.position_indiv, self.predator_position)
            distance = sm.ratio() * len(self.cities)
            vel_fear = r3 * 0.1*len(self.cities)*math.exp(-(10/len(self.cities) * distance))
        
        total_velocity = vel_cognitive + vel_social + vel_personal + vel_fear

        self.personal_section = math.floor(
            len(self.position_indiv) * (vel_personal / total_velocity))
        if vel_cognitive > 0:
            self.cognitive_section = math.floor(
                len(self.position_indiv) * (vel_cognitive / total_velocity))
        if vel_social > 0:
            self.social_section = math.floor(
                len(self.position_indiv) * (vel_social / total_velocity))
        if vel_fear > 0:
            self.fear_section = math.floor(
                len(self.position_indiv) * (vel_fear / total_velocity))
        if len(self.position_indiv) > 52:

    # update the particle position based off new velocity updates
    def update_position(self, pos_best_local):
        personal_start_index = random.randint(
            0, len(self.pos_best_indiv) - self.personal_section)
        cognitive_start_index = random.randint(
            0, len(self.pos_best_indiv) - self.cognitive_section)
        social_start_index = random.randint(
            0, len(self.pos_best_indiv) - self.social_section)
        fear_start_index = random.randint(
            0, len(self.pos_best_indiv) - self.fear_section)

        availability_mask = [True for _ in range(len(self.pos_best_indiv))]
        personal_mask = [True if personal_start_index < x < personal_start_index +
                         self.personal_section else False for x in range(len(self.pos_best_indiv))]
        cognitive_mask = [True if cognitive_start_index < x < cognitive_start_index +
                          self.cognitive_section else False for x in range(len(self.pos_best_indiv))]
        social_mask = [True if social_start_index < x < social_start_index +
                       self.social_section else False for x in range(len(self.pos_best_indiv))]
        fear_mask = [True if fear_start_index < x < fear_start_index +
                       self.fear_section else False for x in range(len(self.pos_best_indiv))]
        new_position = []

        aux_mask = []
        for x, y in zip(
                availability_mask, personal_mask):
            if x and y:
                aux_mask.append(True)
            else:
                aux_mask.append(False)
        for i in self.position_indiv:
            if aux_mask[i]:
                new_position.append(i)
        availability_mask = [
            x ^ y for x, y in zip(
                availability_mask, aux_mask)]
        if len(new_position) > 52:

        aux_mask = []
        for x, y in zip(
                availability_mask, cognitive_mask):
            if x and y:
                aux_mask.append(True)
            else:
                aux_mask.append(False)
        for i in self.pos_best_indiv:
            if aux_mask[i]:
                new_position.append(i)
        availability_mask = [
            x ^ y for x, y in zip(
                availability_mask, aux_mask)]
        if len(new_position) > 52:

        aux_mask = []
        for x, y in zip(
                availability_mask, social_mask):
            if x and y:
                aux_mask.append(True)
            else:
                aux_mask.append(False)
        for i in pos_best_local:
            if aux_mask[i]:
                new_position.append(i)
        availability_mask = [
            x ^ y for x, y in zip(
                availability_mask, aux_mask)]
        if len(new_position) > 52:

        aux_mask = []
        for x, y in zip(
                availability_mask, fear_mask):
            if x and y:
                aux_mask.append(True)
            else:
                aux_mask.append(False)
        for i in reversed(self.predator_position):
            if aux_mask[i]:
                new_position.append(i)
        availability_mask = [
            x ^ y for x, y in zip(
                availability_mask, aux_mask)]

        random.shuffle(self.position_indiv)
        for x in self.position_indiv:
            if availability_mask[x]:
                new_position.append(x)
        if len(new_position) > 52:
        self.position_indiv = new_position


class ParticleSwarm():
    def __init__(self, costFunc, x0, dicio, num_particles,
                 time_budget, weight, cognitive_param, social_param):
        global num_dimensions

        num_dimensions = len(x0)
        err_best_g = -1                   # best error for group
        pos_best_g = []                   # best position for group
        self.best_individuals = []
        self.fitness_averages = []
        self.population_initialization_time = 0.0
        self.generation_calculation_times = []
        random_immigrant = 0 / num_particles
        # establish the swarm
        swarm = []
        predator = Predator(dicio)
        start = timer()
        for i in range(num_particles):
            swarm.append(Particle(dicio))
            swarm[-1].predator_position = predator.position_indiv
        end = timer()
        self.population_initialization_time = end - start
        # begin optimization loop
        i = 0
        budget = timer()
        budget_end = timer()
        while (budget_end - budget) < time_budget:
            # cycle through particles in swarm and evaluate fitness
            average_fitness = 0.0
            self.generation_calculation_times.append(0)

            for j in range(num_particles):
                if random_immigrant > random.random():
                    swarm[j] = Particle(dicio)
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

            predator.update_velocity()
            predator.update_position(pos_best_g)
            # cycle through swarm and update velocities and position
            for j in range(num_particles):
                t2_start = timer()
                swarm[j].predator_position = predator.position_indiv
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
            budget_end = timer()

        print('FINAL:')
        print(pos_best_g)
        print(err_best_g)
