import random

chromosome_length_max = 8
current_generations = 0
max_generations = 4
population_current = list()
population_count = 0
population_max = 4
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

if len(population_current) == 0:
  while population_count < population_max:
    population_count = population_count + 1
    population_current.append(chromosome())

print len(population_current)
print population_current