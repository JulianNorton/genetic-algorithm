import random
import sys

################################################################

# random.seed(1)

chromosome_length_max = 16

solution = '1' * chromosome_length_max

max_generations = 2

population_max = 8

epoch_runs = 2

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

def population_reproduction():
    population_survivors = list()
    for k, v in population_current:
        population_survivors.append(v)
    for parent_a, parent_b in zip(*[iter(population_survivors)]*2):
        child_a = list()
        child_b = list()
        # randomy select which gene to take from parent
        for i in xrange(len(parent_a)):
            if random.randint(0,1) == 0:
                child_a += str(parent_a[i])
            else:
                child_a += str(parent_b[i])

        for i in xrange(len(parent_b)):
            if random.randint(0,1) == 0:
                child_b += str(parent_a[i])
            else:
                child_b += str(parent_b[i])

        child_a = ''.join(child_a)
        child_b = ''.join(child_b)

        child_a = chromosome_mutation(child_a)
        child_b = chromosome_mutation(child_b)

        chromosome_scored = chromosome_fitness(child_a), child_a
        population_current.append(chromosome_scored)

        chromosome_scored = chromosome_fitness(child_b), child_b
        population_current.append(chromosome_scored)

def population_reproduction_zipper():
    population_survivors = list()
    for k, v in population_current:
        population_survivors.append(v)
    # 'Zipper' style, e.g. child_a == 'ABAB', child_b = 'BABA'
    for parent_a, parent_b in zip(*[iter(population_survivors)]*2):
        child_a = list()
        child_b = list()
        for i in xrange(len(parent_a) / 2):
            child_a += parent_a[i] + parent_b[i]
            child_b += parent_b[i] + parent_a[i]

        child_a = ''.join(child_a)
        child_b = ''.join(child_b)

        child_a = chromosome_mutation(child_a)
        child_b = chromosome_mutation(child_b)

        chromosome_scored = chromosome_fitness(child_a), child_a
        population_current.append(chromosome_scored)

        chromosome_scored = chromosome_fitness(child_b), child_b
        population_current.append(chromosome_scored)

def population_reproduction_zipper_b():
    population_survivors = list()
    for k, v in population_current:
        population_survivors.append(v)
    # Pairing the top parents together. e.g. (A,B), (C,D)
    for parent_a, parent_b in zip(*[iter(population_survivors)]*2):
        # Creating empty lists to append to
        child_a, child_b = [], []
        # Child_a, 'Wild'! Randomly selects from either parent for every gene
        for i in xrange(len(parent_a)):
            if random.randint(0,1) == 0:
                child_a += str(parent_a[i])
            else:
                child_a += str(parent_b[i])

        # Child_b 'Zipper'! e.g. child_b = 'BABA . . .'
        for i in xrange(len(parent_b) / 2):
            child_b += parent_a[i] + parent_b[i]
        # Converting the children lists back to strings
        # Randomly mutate each child
        child_a, child_b = chromosome_mutation(''.join(child_a)), chromosome_mutation(''.join(child_b))
        # Adding a fitness score to child A
        # Inserting child A into the population
        population_current.append((chromosome_fitness(child_a), child_a))
        # Same thing for child B
        population_current.append((chromosome_fitness(child_b), child_b))

def population_fitness_average():
    fitness_list = list()
    top_fitness = 0
    for fitness, individual in population_current:
        fitness_list.append(fitness)
        if top_fitness < fitness:
            top_fitness = fitness
    print 'Top generation fitness ==', top_fitness
    print 'Average Fitness ==', sum(fitness_list) / len(fitness_list)

def solution_checker():
    for fitness, individual in population_current:
        if individual == solution:
            # population_status()
            population_fitness_average()
            print '******************'
            print '--------------------'
            print 'SOLUTION FOUND!'
            print '--------------------'
            print '******************'

def generation_iterate():
    population_sorted()
    population_cull()
    population_reproduction_zipper_b()
    solution_checker()

def epoch_generate(x):
    population_current = list()
    population_generate()
    for i in xrange(x):
        print '******************'
        print '--------------------'
        print 'Beginning new epoch'
        print '--------------------'
        print '******************'
        for i in xrange(max_generations):
            generation_iterate()
            population_fitness_average()
            print 'Generation count ==', i
        # population_status()
        # print 'no solution found'
    sys.exit(0)


epoch_generate(epoch_runs)

