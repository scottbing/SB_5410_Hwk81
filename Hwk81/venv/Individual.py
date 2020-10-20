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
        #pix = numpy.random.rand(100,100,3) * 255        # jake.jpg
        #pix = numpy.random.rand(150,200,3) * 255        # fruit.jpg
        pix = numpy.random.rand(38, 50, 3) * 255      # tinyfruit.jpg
        return pix

    def mate(self, par2):
        '''
            Perform half mating and produce new offspring
        '''
        # chromosome for offspring
        length = len(self.chromosome)

        # toggle placement of offspring
        # take half of one parent and half of another to make child
        k = random.randint(0, 1)
        if k == 1:
            child_chromosome = \
                numpy.concatenate((self.chromosome[0:int(length / 2)], par2.chromosome[int(length / 2):]))
        else:
            child_chromosome = \
                numpy.concatenate((par2.chromosome[0:int(length / 2)], self.chromosome[int(length / 2):]))

        # add random mutation
        # prob = random.random()
        # if prob < 0.4:
        #     idx = random.randint(0,length-1)
        #     child_chromosome[idx] = self.mutated_genes()

        # create new Individual(offspring) using
        # generated chromosome for offspring
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
                if int(gs[0]) != gt[0] and int(gs[1]) != gt[1] and int(gs[2]) != gt[2]:
                    fitness += 1
        return fitness
