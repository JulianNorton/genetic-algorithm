import random
import sys

################################################################

# random.seed(1)

chromosome_length_max = 64

max_generations = 100000

population_max = 1024
population_current = list()

mutation_chance = random.randint(0,1) # 10%
gene_replacement = random.randint(0,1)
gene_replacement = '1'


solution = '1' * chromosome_length_max
################################################################

def chromosome():
  gene = ""
  for i in xrange(chromosome_length_max):
      gene += str(random.randint(0,1))
  return gene

def chromosome_fitness(x):
  chromosome_fitness = float(x.count('1')) / float(chromosome_length_max)
  return chromosome_fitness

# test = list()
def population_generate():
  for i in xrange(population_max):
    key = chromosome()
    chromosome_scored = chromosome_fitness(key), key
    population_current.append(chromosome_scored)

def population_sorted():
  population_current.sort(reverse=True)

def population_status():
  print population_current
  # print len(population_current)
  print 'pop count ==', len(population_current)

def population_cull():
  i = 0
  while i < (population_max / 2):
    del population_current[-1]
    i = i + 1


def chromosome_mutation(chromosome):
    chromosome = list(chromosome)
    gene_location = random.randint(0,(chromosome_length_max - 1))
    if mutation_chance == 0:
      chromosome[gene_location] = str(gene_replacement)
      chromosome = ''.join(chromosome)
      return chromosome
    else:
      chromosome = ''.join(chromosome)
      return chromosome

def population_reproduction():
  population_survivors = list()
  for k, v in population_current:
    population_survivors.append(v)
  for parent_A, parent_B in zip(*[iter(population_survivors)]*2):
    child_A = parent_A[:(chromosome_length_max/2)] + parent_B[(chromosome_length_max/2):chromosome_length_max]
    child_A = chromosome_mutation(child_A)
    chromosome_scored = chromosome_fitness(child_A), child_A
    population_current.append(chromosome_scored)
    child_B = parent_B[:(chromosome_length_max/2)] + parent_A[(chromosome_length_max/2):chromosome_length_max]
    child_B = chromosome_mutation(child_B)
    chromosome_scored = chromosome_fitness(child_B), child_B
    population_current.append(chromosome_scored)

def population_fitness_average():
  fitness_list = list()
  for k, v in population_current:
    fitness_list.append(k)
  # print 'Fitness list:', fitness_list
  print 'Average Fit ==', sum(fitness_list) / len(fitness_list)
  # print 'test'

  # print 'survivors', population_survivors

def solution_checker():
  for k, v in population_current:
    # print v
    if v == solution:
      population_status()
      population_fitness_average()
      print '******************'
      print '--------------------'
      print 'SOLUTION FOUND!'
      print '--------------------'
      print '******************'
      sys.exit(0)

def generation_iterate():
    population_cull()
    population_reproduction()
    population_sorted()
    solution_checker()

def epoch_generate():
  population_generate()
  population_sorted()
  for i in xrange(max_generations):
    generation_iterate()
    population_fitness_average()
    print 'Generation count ==', i
  population_status()

epoch_generate()

