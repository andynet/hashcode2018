from pyeasyga import pyeasyga
import random
import sys
import numpy as np





class Debug(pyeasyga.GeneticAlgorithm):

    def run(self):
        self._i = 0
        super(Debug, self).run()

    def create_next_generation(self):
        self._i += 1
        print("NextGeberation %d" % self._i)
        super(Debug, self).create_next_generation()

def load_data(model):
    data = []
    for cache in range(model._numCaches):
        for video in range(model._numVideos):
            data.append({'video':video, 'cache':cache})
    return data



if len(sys.argv) < 4:
    print("Usage: %s <file> <population> <generations>" % sys.argv[0])
    sys.exit(0)

data = []
population = int(sys.argv[2])
generation = int(sys.argv[3])



ga = Debug(data,
        maximise_fitness = True,
        elitism = True,
        population_size = population,
        generations = generation)


def create_individual(data):
    return np.zeros(shape=(data.N), dtype=np.int32)


def crossover(parent_1, parent_2):
    index = random.randrange(1, len(parent_1) - 1)
    child_1 = np.concatenate(parent_1[index:], parent_2[:index])
    child_2 = np.concatenate(parent_1[:index], parent_2[index:])
    return child_1, child_2


def mutate(individual):
    global data
    index = random.randrange(len(individual))
    individual[index] = random.randrange(0, data.F)
    

def fitness(individual, data):
    pass


ga.fitness_function = fitness

ga.create_individual = create_individual

ga.crossover_function = crossover

ga.mutate_function = mutate

ga.run()

print(ga.best_individual())







