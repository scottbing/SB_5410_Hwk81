import random
import numpy


class Individual(object):
    '''
    Class representing individual in population
    '''

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()
        self.genes = None
        self.target = None

    @classmethod
    def set_genes(self, genes):
        self.genes = genes

    @classmethod
    def set_target(self, target):
        self.target = target

    @classmethod
    def mutated_genes(self):
        '''
        create random genes for mutation
        '''
        r = random.choice(range(0, 255))
        g = random.choice(range(0, 255))
        b = random.choice(range(0, 255))
        return (r, g, b)

    @classmethod
    def create_gnome(self):
        '''
        create chromosome or string of genes
        '''
        pix = numpy.random.rand(100,100,3) * 255
        return pix

    def halfmate(self, par2):
        '''
            Perform half mating and produce new offspring
        '''
        # chromosome for offspring
        length = len(self.chromosome)

        child_chromosome = self.chromosome[0:int(length/2)] + par2.chromosome[int(length/2):]
        prob = random.random()
        if prob < 0.5:
            idx = random.randint(0,(length/2)-1)
            print("halfmate length: ", length)
            print("idx: ", idx)
            child_chromosome[idx] = self.mutated_genes()

        # create new Indidual(offspring) using
        # generated chomosome for offspring
        return Individual(child_chromosome)

    def cal_fitness(self):
        '''
        Calculate fittness score, it is the number of
        characters in string which differ from target
        string.
        '''
        fitness = 0
        for rows, rowt in zip(self.chromosome, self.target):
            for gs,gt in zip(rows, rowt):
                if int(gs[0]) != gt[0] and\
                        int(gs[1]) != gt[1] and\
                        int(gs[2]) != gt[2]:
                    fitness += 1
        return fitness
