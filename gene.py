from pyeasyga import pyeasyga
import random
import sys
import numpy as np
import parser
import grader



class Debug(pyeasyga.GeneticAlgorithm):

    def run(self):
        self._i = 0
        super(Debug, self).run()

    def create_next_generation(self):
        self._i += 1
        print("NextGeberation %d" % self._i)
        super(Debug, self).create_next_generation()


if len(sys.argv) < 3:
    print("Usage: %s <population> <generations>" % sys.argv[0])
    sys.exit(0)

data = parser.parse()
population = int(sys.argv[1])
generation = int(sys.argv[2])



ga = Debug(data,
        maximise_fitness = True,
        elitism = True,
        population_size = population,
        generations = generation)


def create_individual(data):
    return np.zeros(shape=(data.N), dtype=np.int32)


def crossover(parent_1, parent_2):
    index = random.randrange(1, len(parent_1) - 1)
    child_1 = np.append(parent_1[index:], parent_2[:index])
    child_2 = np.append(parent_1[:index], parent_2[index:])
    return child_1, child_2


def mutate(individual):
    global data
    #if np.sum(individual) > 0:
    #    print(individual)
    for i in range(len(individual)//10):
        index = random.randrange(len(individual))
        individual[index] = random.randrange(0, data.F + 1)
    

def fitness(individual, data):
    conv_ind, x = parser.converter(data, individual)
    return grader.rate(data, conv_ind) 


ga.fitness_function = fitness

ga.create_individual = create_individual

ga.crossover_function = crossover

ga.mutate_function = mutate

ga.run()



best = ga.best_individual()
print(best)

x, best = parser.converter(data, best[1])
print(best)
parser.vystupConverted(best)







