# numpy used for random generation and percentile function
#import numpy as np
import random

population = []
generation_count = 0
solution = '11111111'


class Individual (object):
    class Chromosome(object):
        def __init__(self, length=0, length_max=8):
            # create a string that's made up of random bits
            gene = ""
            # Append '0' or '1' until max
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
            print self.individuals[i].calculate_fitness()
            i = i + 1
            # print i, "count #"
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


current_population = Population()

current_population.sort_by_fitness()

current_population.dump_individuals(20)

# current_population.kill_some_population()

# print "########################################################"
# current_population.dump_individuals(10)

# print "########################################################"

# for i in xrange(0, 11, 2):
#     print(i)
# gene_length = len(current_population.individuals[0].chromosome.gene)
# print "gene length = ", gene_length
# half_gene_length = gene_length / 2
# print "1/2 gene length = ", half_gene_length

# print current_population.individuals[19].chromosome.gene
# print "A1 | 1st half |", current_population.individuals[19].chromosome.gene[0:(half_gene_length)]
# A1 = current_population.individuals[19].chromosome.gene[0:(half_gene_length)]
# print "A2 | 2nd half |", current_population.individuals[19].chromosome.gene[(half_gene_length):]
# A2 = current_population.individuals[19].chromosome.gene[0:(half_gene_length)]


# print current_population.individuals[18].chromosome.gene
# print "B1 | 1st half |", current_population.individuals[18].chromosome.gene[0:(half_gene_length)]
# B1 = current_population.individuals[18].chromosome.gene[0:(half_gene_length)]
# print "B2 | 2nd half |", current_population.individuals[18].chromosome.gene[(half_gene_length):]
# B2 = current_population.individuals[18].chromosome.gene[0:(half_gene_length)]

# child1 = A1 + B2
# print "parent 1 <---->", A1+A2
# print "parent 2 <---->", B1+B2
# print "child  1 <---->", child1

# child2 = B1 + A2
# print "child  2 <---->", child2

# # print len(current_population.individuals)

# x = range(5)

# print x


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# overloading operators
# print population
# could just do what dump is doing

def check_solution():
    global generation_count
    global solution
    if solution in population:
        print generation_count
    else:
        generation_count = generation_count + 1
        print "no solution"
        print generation_count, "generation"

# print ""
# print "----------------------"
# print "| testing code below |"
# print "----------------------"
# print ""


# test = generate_chromosome()
# print test[0:4], "|", test[4:8], "|| parent 1"
# test1 = generate_chromosome()
# print test1[0:4], "|", test1[4:8], "|| parent 2"
# # take first 4 digits from parent 1, and last 4 from parent 2
# test2 = test[0:4] + test1[4:8]
# print test2[0:4], "|", test2[4:8], "|| child 1"
# # take first 4 digits from parent 2, and last 4 from parent 1
# test3 = test1[0:4] + test[4:8]
# print test3[0:4], "|", test3[4:8], "|| child 2"


# def gene_mutation():
#     # 2% chance to randomly mutate a bit
#     # if random.randint(0,49) == 0:
#     if random.randint(0,0) == 0:
#         global test3
#         print "Mutation triggered!"
#         print test3
#         test3 = test3[4].replace('0','1')
#         print test3
#     else:
#         print "No mutation"

# gene_mutation()

