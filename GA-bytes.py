import random
import sys

### Variables
current_generations = 0
solution_found = False
max_generations = 1000
solution = '1111111111111111'
gene_replacement = random.randint(0,1)
mutation_chance = random.randint(0,19)
# Need to make these variables dynamic to the chromosome length
gene_location = random.randint(0,15)
def create_survivors_population():
    # Making a new iterable list to reproduce, else tuples throws an error
    global survivors_population
    survivors_population = [] 

def use_survivors_population():
    return survivors_population
create_survivors_population()

# Classes & Objects #

class Individual (object):
    class Chromosome(object):
        def __init__(self, length=0, length_max=16):
            # create a string that's made up of random bits
            # Append '0' or '1' until max
            gene = ""
            for i in xrange(length_max):
                gene += str(random.randint(0,1))
            else:
                self.gene = gene
                self.length_max = length_max
            # gene += (str(random.randint(0,1))

    def __init__(self):
        self.chromosome = self.Chromosome()
    def calculate_fitness(self):
        # Counts the number of '1s' and returns the ratio
        fitness = float(self.chromosome.gene.count('1')) / float(self.chromosome.length_max)
        return fitness

class Population(object):
    def __init__(self, count=0, length_max=20):
        self.individuals = []
        population_count = 0
        while population_count < length_max:
            population_count = population_count + 1
            self.individuals.append(Individual())
    def sort_by_fitness(self):
        fitnesses = []
        for individual in self.individuals:
            fitnesses.append(individual.calculate_fitness())
        sorted_fitness_and_individuals = sorted(zip(fitnesses, self.individuals))
        fitness_trash, self.individuals = zip(*sorted_fitness_and_individuals)
    def dump_individuals(self, count=10):
        i = 0
        while i < count:
            print self.individuals[i].chromosome.gene
            # print self.individuals[i].calculate_fitness()
            i = i + 1
    def kill_some_population(self, count=10):
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
    for parent_A, parent_B in zip(*[iter(survivors_population)]*2):
      child_A = parent_A[0:8] + parent_B[8:16]
      child_A = gene_mutation(child_A)
      child_B = parent_B[0:8] + parent_A[8:16]
      child_B = gene_mutation(child_B)
      survivors_population.extend([child_A, child_B])

# 5% chance to randomly mutate a bit
def gene_mutation(chromosome):
    chromosome = list(chromosome)
    for i in chromosome[gene_location]:
        if mutation_chance == 0:
            chromosome[gene_location] = str(gene_replacement)
            chromosome = ''.join(chromosome)
            return chromosome
        else:
            chromosome = ''.join(chromosome)
            return chromosome

def solution_checker():
    for i in current_population:
        if i == solution:
            print '******************'
            print '--------------------'
            print 'SOLUTION FOUND! ==', '\'1111111111111111\''
            print 'from generation', current_generations
            print survivors_population
            print '--------------------'
            print '******************'
            sys.exit(0)
        else:
            print 'no solution:'
            print 'current_generations ==', current_generations
            print 'current population size ==', len(current_population)
            print ''

def reproduction_setup():
    use_survivors_population()
    for individual in current_population.individuals:
        survivors_population.append(individual.chromosome.gene)

# EXECUTES THE SEARCH!
# Sloppy, but it works!
while solution_found == False and current_generations < max_generations:
    current_generations = current_generations + 1
    current_population = Population()
    current_population.sort_by_fitness()
    current_population.kill_some_population()
    reproduction_setup()
    reproduction()
    current_population = survivors_population
    solution_checker()
    survivors_population = list()
    if current_generations == max_generations:
        print 'final population'
        print current_population

