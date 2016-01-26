# numpy used for random generation and percentile function
#import numpy as np
import random

population = []
population_count = 0
chromosome_length_max = 8.0
chromosome_length = 0.0
generation_count = 0
solution = '11111111'

def generate_chromosome():
    #print "chromosome"
    chromosome_length = 0
    gene = ""
    while chromosome_length < chromosome_length_max:
        chromosome_length += 1
        #print str(chromosome_length) + " bit count"
        #print gene + " current gene"

        if random.randint(0,1) == 0:
            gene += '0'
            #print gene
        else:
            gene = gene + '1'
            #print gene
    else:
        #print "bit count at 8"
        # print "[1] count:"
        # print gene.count('1')
        return gene



def fitness_calc():
    fitness_score = 0
    fitness_score = population[0].count('1') / chromosome_length_max
    print "Fitness score:"
    print fitness_score
    # print fitness_score



def check_solution():
    global generation_count
    global solution
    if solution in population:
        print generation_count
    else:
        generation_count = generation_count + 1
        print "no solution"
        print generation_count, "generation"


def generate_population():
    population_count = 0
    while population_count < 4:
        population_count = population_count + 1
        population.append(generate_chromosome())

generate_population()

print population
check_solution()

print ""
print "----------------------"
print "| testing code below |"
print "----------------------"
print ""


test = generate_chromosome()
print test[0:4], "|", test[4:8], "|| parent 1"
test1 = generate_chromosome()
print test1[0:4], "|", test1[4:8], "|| parent 2"
# take first 4 digits from parent 1, and last 4 from parent 2
test2 = test[0:4] + test1[4:8]
print test2[0:4], "|", test2[4:8], "|| child 1"
# take first 4 digits from parent 2, and last 4 from parent 1
test3 = test1[0:4] + test[4:8]
print test3[0:4], "|", test3[4:8], "|| child 2"


def gene_mutation():
    # 2% chance to randomly mutate a bit
    # if random.randint(0,49) == 0:
    if random.randint(0,0) == 0:
        global test3
        print "Mutation triggered!"
        print test3
        test3 = test3[4].replace('0','1')
        print test3
    else:
        print "No mutation"

gene_mutation()



##########################
# Unfinished notes below #
##########################


#{"key2":"I am a string", "new key":"New value", "key1":[1,2,3],123:456}

# def generate_species():
#     # 20 times in for loop (?)
#     species_count = 0
#     while species_count < 20:
#         #each member of the species should be 1 random gene
#         # +1 chromosome to species dictionary?
#         species_count = species_count + 1
#         print species_count
#     else:
#         print "species at max (20)"

#generate_species()

# y = ['1', '2' ,'3' ,'4' ,'5']
# print y[2].count('1')

#def fitness_calc():
    #print "fitness_calc"
    # count 1's in species
    # divide count by 8 (gene length)
    # assign fitness score
    # e.g, [1010-0111] would be fitness of 5/8, or .625
    # sort dictionary by ascending (?)
    #list.sort()
    
# def fitness_prune(): 
#     print "fitness_prune"
#     #from species, remove 11-20 from species (bottom 50%)
#     #.slice the fitness_calc array/dict (?)
#     # use NumPy `RESHAPE` instead of slice or percentile?


# def chromosome_pairs():
#     print "chromosome_pairs"
#     # dictionary / key with each pair
#     # form pair[1]
#         # take #1 from fitness calc
#         # take #2 from fitness calc
#     # form pair[2]
#         # take #3 from fitness calc
#         # take #4 from fitness calc
#     # etc..., until 5 pairs.

# def crossover_chromosomes():
#     print "crossover_genes"
#     # with newly created key pairs from remaining world pop
#     # generate 2 new children chromosomes from each chromosomes_pair
#         #take species[1] and species[2]
#             # take first 4 bits from chromosome[1]
#                 # append to a new chromosome
#             # take last 4 bits from chromosome[2]
#                 # append to a new chromosome
#             #check for chromosome_mutation()

#             # take first 4 bits from chromosome[2]
#                 # append to a new chromosome
#             # take last 4 bits from chromosome[1]
#                 # append to a new chromosome
#     # run chromosome_mutation()
#     # add new chromosome to species_pop dict
#     # repeat for remaining chromosome pair.

# def chromosome_mutation():
#     # 2% chance to randomly mutate a bit
#     if random.randint(0,49) == 0:
#         print "Mutation triggered!"
#         # random.randint(0,7) == 0:...
#             # whatever random integer it picks, flip that bit
#             # e.g. random.randint(0,7) == 0
#                 # 0000000[1] => 0000000[0]
#             # else 1 = 0 
#     else:
#         print "No mutation"

#LOOP! goto fitness calc if no solution found
