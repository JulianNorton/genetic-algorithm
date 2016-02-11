#  ADD MORE PRINT STATEMENTS EVERYWHERE !!

import random
import sys

### Variables
current_generations = 0
solution_found = False
max_generations = 4
solution = '11111111111111111111111111111111'
# gene_replacement = random.randint(0,1)
gene_replacement = 'GENE REPLACEMENT'
mutation_chance = random.randint(0,24)
# Need to make these variables dynamic to the chromosome length
def create_survivors_population():
    # Making a new iterable list to reproduce, else tuples throws an error
    global survivors_population
    survivors_population = [] 

def use_survivors_population():
    return survivors_population

create_survivors_population()

# Classes & Objects #


chromosome_length_max = 32

class Individual (object):
    class Chromosome(object):
        def __init__(self, length=0):
            # create a string that's made up of random bits
            # Append '0' or '1' until max
            gene = ""
            for i in xrange(chromosome_length_max):
                gene += str(random.randint(0,1))
            else:
                self.gene = gene
                self.chromosome_length_max = chromosome_length_max
            # gene += (str(random.randint(0,1))

    def __init__(self):
        self.chromosome = self.Chromosome()
    def calculate_fitness(self):
        # Counts the number of '1s' and returns the ratio
        fitness = float(self.chromosome.gene.count('1')) / float(chromosome_length_max)
        return fitness

class Population(object):
    def __init__(self, count=0, length_max=4, individuals=[]):
        self.individuals = individuals
        population_count = 0
        # print len(individuals), ' :)))'
        if len(individuals) == 0:
            while population_count < length_max:
                population_count = population_count + 1
                self.individuals.append(Individual())
    def get_individuals(self):
        return self.individuals
    def sort_by_fitness(self, length_max=20):
        fitnesses = []
        overall_fitness = 0
        for individual in self.individuals:
            fitnesses.append(individual.calculate_fitness())
            overall_fitness = overall_fitness + individual.calculate_fitness()
            # print individual.calculate_fitness(), 'individual.calculate_fitness()'

        overall_fitness = overall_fitness / length_max
        print 'Average fitness ==', overall_fitness
        sorted_fitness_and_individuals = sorted(zip(fitnesses, self.individuals))
        fitness_trash, self.individuals = zip(*sorted_fitness_and_individuals)
    # def dump_individuals(self, count=10):
    #     i = 0
    #     while i < count:
    #         print self.individuals[i].chromosome.gene
    #         # print self.individuals[i].calculate_fitness()
    #         i = i + 1
    def kill_some_population(self, count=2):
        fitnesses = []
        for individual in self.individuals:
            fitnesses.append(individual.calculate_fitness())
        sorted_fitness_and_individuals = sorted(zip(fitnesses, self.individuals))
        i = 0
        while i < count:
            del sorted_fitness_and_individuals[i]
            i = i + 1
        fitness_trash, self.individuals = zip(*sorted_fitness_and_individuals)

# Back to simple functions!

# Need to make the splits dynamic to the chromosome length
def reproduction():
    print survivors_population, 'survivors_population'
    for parent_A, parent_B in zip(*[iter(survivors_population)]*2):
      child_A = parent_A[0:(len(parent_A) / 2)] + parent_B[(len(parent_A) / 2):len(parent_B)]
      child_A = gene_mutation(child_A)
      child_B = parent_B[0:(len(parent_B) / 2)] + parent_A[(len(parent_B) / 2):len(parent_A)]
      child_B = gene_mutation(child_B)
      print survivors_population, 'survivors_population'
      print child_A, 'child a'
      print child_B, 'child b'
      survivors_population.extend([child_A, child_B])
      print '**'
      print survivors_population
      print len(survivors_population)
      print '**'

# 5% chance to randomly mutate a bit (though really 2.5%)
def gene_mutation(chromosome):
    chromosome = list(chromosome)
    gene_location = random.randint(0,(chromosome_length_max - 1))
    for i in chromosome[gene_location]:
        if mutation_chance == 0:
            chromosome[gene_location] = str(gene_replacement)
            chromosome = ''.join(chromosome)
            return chromosome
        else:
            chromosome = ''.join(chromosome)
            return chromosome

def solution_checker():
    for i in current_population.get_individuals():
        if i == solution:
            print '******************'
            print '--------------------'
            print 'SOLUTION FOUND! ==', '\'1111111111111111\''
            print 'from generation', current_generations
            print survivors_population
            print '--------------------'
            print '******************'
            sys.exit(0)


def reproduction_setup():
    use_survivors_population()
    for individual in current_population.individuals:
        survivors_population.append(individual.chromosome.gene)

# EXECUTES THE SEARCH!
# Sloppy, but it works!
first_run = False
if first_run == False:
        current_population = Population()
        current_population.sort_by_fitness()


while solution_found == False and current_generations < max_generations:
    current_generations = current_generations + 1
    print current_generations, 'current generation'
    print len(current_population.get_individuals()), 'len(current_population)'
    current_population.sort_by_fitness()
    current_population.kill_some_population()
    # reproduction_setup(), Probably breaking everything
    reproduction_setup()
    reproduction()
    current_population = Population(survivors_population)
    solution_checker()
    survivors_population = list()
    if current_generations == max_generations:
        print 'final population'
        # print current_population.get_individuals()

