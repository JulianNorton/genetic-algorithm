# numpy used for random generation and percentile function
#import numpy as np
import random

# used to quit the program once a solution is found
import sys


byte = ""

def generate_chromosome():
    print "chromosome! ##############################################"
    bit_count = 0
    byte = ""
    while bit_count < 8:
        bit_count += 1
        #print str(bit_count) + " bit count"
        #print byte + " current byte"
        if random.randint(0,1) == 0:
            byte += '0'
            #print byte
        else:
            byte = byte + '1'
            #print byte
    else:
        #print "bit count at 8"
        fitness_score = 0
        fitness_score = float(byte.count('1') / 8.0)
        print byte
        print "[1] count:"
        print byte.count('1')
        print "Fitness score:"
        print fitness_score

generate_chromosome()

##########################
# Unfinished notes below #
##########################



def generate_species():
    # 20 times in for loop (?)
    species_count = 0
    while species_count < 20:
        #each member of the species should be 1 random byte
        # +1 chromosome to species dictionary?
        species_count = species_count + 1
        print species_count
    else:
        print "species at max (20)"

#generate_species()

def fitness_calc():
    print "fitness_calc"
    # count 1's in species
    # divide count by 8 (byte length)
    # assign fitness score
    # e.g, [1010-0111] would be fitness of 5/8, or .625
    # sort dictionary by ascending (?)
    list.sort()
    
def fitness_prune(): 
    print "fitness_prune"
    #from species, remove 11-20 from species (bottom 50%)
    #.slice the fitness_calc array/dict (?)
    # use NumPy `RESHAPE` instead of slice or percentile?


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

def crossover_chromosomes():
    print "crossover_genes"
    # with newly created key pairs from remaining world pop
    # generate 2 new children chromosomes from each chromosomes_pair
        #take species[1] and species[2]
            # take first 4 bits from chromosome[1]
                # append to a new chromosome
            # take last 4 bits from chromosome[2]
                # append to a new chromosome
            #check for chromosome_mutation()

            # take first 4 bits from chromosome[2]
                # append to a new chromosome
            # take last 4 bits from chromosome[1]
                # append to a new chromosome
    # run chromosome_mutation()
    # add new chromosome to species_pop dict
    # repeat for remaining chromosome pair.

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

def check_solution():
    #if any chromosome in species = 11111111:
        print "solution found!"
        sys.exit("Error message")
    #else:
        print "no solution"

#LOOP! goto fitness calc if no solution found
