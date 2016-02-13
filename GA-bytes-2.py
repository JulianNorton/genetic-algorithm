import random

chromosome_length_max = 8
current_generations = 0
max_generations = 4
population_max = 40
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
    value = chromosome_fitness(key)
    key_value = key, value
    population_current.append(key_value)

population_generate()

print population_current




# population_current = population_current.items()
# print population_current
# population_fitness_chromosome = list()
# for x, y in population_current.items():
#   population_fitness_chromosome.append( (x,y) )
# print population_current

# population_current.sort(reverse=True)

# population_current = population_fitness_chromosome



print 'pop count ==', len(population_current)


def population_cull():
  i = 0
  # while i < (population_max / 2):
  #   # print i
  #   # print population_current[-1]
  #   del population_current[-1]
  #   i = i + 1

# population_cull()
# print len(population_current)

# while i < (population_max / 2):
  # print sorted_fitness_and_individuals[i]
  # del sorted_fitness_and_individuals[i]
  # i = i + 1
# print population_current


