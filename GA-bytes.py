# numpy used for random generation and percentile function
import numpy

# used to quit the program once a solution is found
import sys

world_pop = 0

def fitness_calc():
    print "fitness_calc"
    #count 1's in world_pop
    #divide count by 20 (byte length)
    # assign fitness score
    # e.g, [11111-11111-00000-00000] would be fitness of 5/20, or .25
    #sort dictionary by ascending (?)
    list.sort()
    
def fitness_prune(): 
    print "fitness_prune"
    #from world_pop, remove 11-20 from world_pop (bottom 50%)
    #.slice the fitness_calc array (?)
    # use NumPy `RESHAPE` instead of slice or percentile?

def chromosome():
    print "chromosome"
    # needs to create 1 byte
    # append 0 or 1 randomly 8 times in for loop (?)
    if random.randint(0,1) == 0:
        return 0
    else:
        return 1

def world_pop_generate():
    while world_pop < 20:
        #each member of world pop should be 1 random byte
        # +1 chromosome to world_pop dictionary?
        world_pop = world_pop + 1
        print world_pop
    else:
        print "world_pop at max (20)"

def chromosome_pairs():
    print "chromosome_pairs"
    # dictionary / key with each pair
    # form pair[1]
        # take #1 from fitness calc
        # take #2 from fitness calc
    # form pair[2]
        # take #3 from fitness calc
        # take #4 from fitness calc
    # etc..., until 5 pairs.

def chromosome_mutation():
    # 2% chance to randomly mutate a bit
    if random.randint(0,49) == 0:
        print "Mutation triggered!"
        # random.randint(0,7) == 0:...
            # whatever random integer it picks, flip that bit
            # e.g. random.randint(0,7) == 0
                # 0000000[1] => 0000000[0]
            # else 1 = 0 
    else:
        print "No mutation"


def crossover_chromosomes():
    print "crossover_genes"
    # with newly created key pairs from remaining world pop
    # generate 2 new children chromosomes from each chromosomes_pair
        #take world_pop[1] and world_pop[2]
            # take first 4 bits from chromosome[1]
                # append to a new chromosome
            # take first 4 bits from chromosome[2]
                # append to a new chromosome
            #check for chromosome_mutation()

            # take first 4 bits from chromosome[2]
                # append to a new chromosome
            # take first 4 bits from chromosome[1]
                # append to a new chromosome
    # run chromosome_mutation()
    # append new chromosome to world_pop
    # repeat for remaining chromosome pair.

def check_solution():
    #if any chromosome in world_pop = 11111111:
        print "solution found!"
        sys.exit("Error message")
    #else:
        print "no solution"



