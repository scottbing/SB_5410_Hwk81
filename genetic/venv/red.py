# Python3 program to create target string, starting from
# random string using Genetic Algorithm

import random
from Individual import *

# Valid genes
GENES = range(0,255)

# Target string to be generated
TARGET = "113,23.78.212.203,255,6,55,98,145,200,72,62,183,43,7,112,116,34,58,142,76,184,192,28,101"


# Number of individuals in each generation
POPULATION_SIZE = 100

# Generations limit
G_LIMIT = 100

# Driver code
def main():
    global POPULATION_SIZE

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population
    for i in range(POPULATION_SIZE):
        Individual.set_genes(GENES)
        Individual.set_target(TARGET)
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))
        print("".join(population[i].chromosome))

    while not found:

        # sort the population in increasing order of fitness score
        population = sorted(population, key=lambda x: x.fitness)

        # if the individual having lowest fitness score ie.
        # 0 then we know that we have reached to the target
        # and break the loop
        if population[0].fitness <= 0:
            found = True
            break

        # Otherwise generate new offsprings for new generation
        new_generation = []

        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            if generation == 89:
                print("".join(parent1.chromosome), "-", "".join(parent2.chromosome))
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        print("Generation: {}\tString: {}\tFitness: {}". \
              format(generation,
                     "".join(population[0].chromosome),
                     population[0].fitness))

        generation += 1
        if generation == G_LIMIT:
            break

    print("Generation: {}\tString: {}\tFitness: {}". \
          format(generation,
                 "".join(population[0].chromosome),
                 population[0].fitness))


if __name__ == '__main__':
    main()
