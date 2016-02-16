import random
import sys

################################################################

# random.seed(1)

chromosome_length_max = 512

solution = '1' * chromosome_length_max

max_generations = 2**14

population_max = 16

# Used a few places, so just defining it globally
population_current = list()

################################################################

def chromosome():
  gene = ""
  for i in xrange(chromosome_length_max):
      gene += str(random.randint(0,1))
  return gene

def chromosome_fitness(x):
  chromosome_fitness = float(x.count('1')) / float(chromosome_length_max)
  return chromosome_fitness

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
    # 10%, but in practice it's 5% because mutation can be identical to previous value.
    gene_replacement = random.randint(0,1)
    mutation_chance = random.randint(0,9)
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
    child_A = list()
    child_B = list()
    # randomy select which gene to take from parent
    for i in xrange(len(parent_A)):
      if random.randint(0,1) == 0:
        child_A += str(parent_A[i])
      else:
        child_A += str(parent_B[i])

    for i in xrange(len(parent_B)):
      if random.randint(0,1) == 0:
        child_B += str(parent_A[i])
      else:
        child_B += str(parent_B[i])

    child_A = ''.join(child_A)
    child_B = ''.join(child_B)

    child_A = chromosome_mutation(child_A)
    child_B = chromosome_mutation(child_B)

    chromosome_scored = chromosome_fitness(child_A), child_A
    population_current.append(chromosome_scored)

    chromosome_scored = chromosome_fitness(child_B), child_B
    population_current.append(chromosome_scored)

def population_fitness_average():
  fitness_list = list()
  top_fitness = 0
  for k, v in population_current:
    fitness_list.append(k)
    if top_fitness < k:
      top_fitness = k
  print 'Top generation fitness ==', top_fitness
  print 'Average Fitness ==', sum(fitness_list) / len(fitness_list)

def solution_checker():
  for k, v in population_current:
    if v == solution:
      # population_status()
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
  # population_status()
    print 'no solution found'
epoch_generate()

