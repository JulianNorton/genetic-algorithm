import random
random.seed(1)
chromosome_length_max = 8
current_generations = 0
max_generations = 40
population_max = 8
population_current = list()
# solution = '1' * chromosome_length_max
# gene_replacement = random.randint(0,1)
# mutation_chance = random.randint(0,24)
# solution_found = False

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
  print 'pop count ==', len(population_current)

def population_cull():
  i = 0
  # population_status()
  while i < (population_max / 2):
    # print population_current[-1]
    del population_current[-1]
    i = i + 1

def population_reproduction():
  # population_status()
  population_survivors = list()
  for k, v in population_current:
    population_survivors.append(v)
  for parent_A, parent_B in zip(*[iter(population_survivors)]*2):
    # print parent_A, 'parent A'
    # print parent_B, 'parent B'
    child_A = parent_A[:(chromosome_length_max/2)] + parent_B[(chromosome_length_max/2):chromosome_length_max]
    # child_A = gene_mutation(child_A)
    chromosome_scored = chromosome_fitness(child_A), child_A
    population_current.append(chromosome_scored)
    child_B = parent_B[:(chromosome_length_max/2)] + parent_A[(chromosome_length_max/2):chromosome_length_max]
    # child_B = gene_mutation(child_B)
    chromosome_scored = chromosome_fitness(child_B), child_B
    population_current.append(chromosome_scored)

def population_fitness_average():
  fitness_list = list()
  for k, v in population_current:
    fitness_list.append(k)
  # print 'Fitness list:', fitness_list
  print 'AVERAGE Fit:', sum(fitness_list) / len(fitness_list)
  # print 'test'

  # print 'survivors', population_survivors

population_generate()
def test():
  population_fitness_average()
  population_sorted()
  population_cull()
  population_reproduction()

population_status()
test()
test()
test()
test()
test()
population_status()
print len(population_current)

