import random

population = []
generation_count = 0

class Individual (object):
    class Chromosome(object):
        def __init__(self, length=0, length_max=8):
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
            # print i, "count #"
    def reproduction(self):
        print "test"
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

# current_population.dump_individuals(20)

current_population.kill_some_population()
# current_population.dump_individuals(10)

# 5% chance to randomly mutate a bit
def gene_mutation(chromosome):
    chromosome = list(chromosome)
    gene_location = random.randint(0,7)
    # gene_replacement = random.randint(0,1)
    gene_replacement = '*****'
    mutation_chance = random.randint(0,1)
    for i in chromosome[gene_location]:
        if mutation_chance == 0:
            # print 'mutation!', chromosome
            chromosome[gene_location] = str(gene_replacement)
            chromosome = ''.join(chromosome)
            # print 'after  ||', chromosome
            return chromosome
# 7=11
# Making a new iterable list to reproduce
survivors_population = []
for individual in current_population.individuals:
    survivors_population.append(individual.chromosome.gene)

print "Current pop ==", len(survivors_population)
print survivors_population
print ''

for parent_A, parent_B in zip(*[iter(survivors_population)]*2):
  child_A = parent_A[0:4] + parent_B[4:8]
  child_A = gene_mutation(child_A)
  child_B = parent_B[0:4] + parent_A[4:8]
  # child_B = gene_mutation(child_B)
  survivors_population.extend([child_A, child_B])

print "Current pop ==", len(survivors_population)
print survivors_population
# print survivors_population


# print current_population.individuals[0].chromosome.gene



# for i in xrange(0, 11, 2):
#     print(i)
# gene_length = len(current_population.individuals[0].chromosome.gene)
# print "gene length = ", gene_length
# half_gene_length = gene_length / 2
# print "1/2 gene length = ", half_gene_length

# print "A1 | 1st half |", current_population.individuals[19].chromosome.gene[0:(half_gene_length)]
# A1 = current_population.individuals[19].chromosome.gene[0:(half_gene_length)]
# print "A2 | 2nd half |", current_population.individuals[19].chromosome.gene[(half_gene_length):]
# A2 = current_population.individuals[19].chromosome.gene[0:(half_gene_length)]

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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# overloading operators
# print population
# could just do what dump is doing

