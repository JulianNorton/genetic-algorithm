## 1. Start
**Generate random population of n chromosomes (suitable solutions for the problem)**
  * 20 random 20 binary sequences: 00100-10100-10010-00100


### 2. Fitness
**Evaluate the fitness f(x) of each chromosome x in the population
all 1's are correct.**
* Count 1's in sequences
* Sort descending, higher count of 1's are on top, higher count of 0's are bottom.
* Bottom 50% die.

### 3. New population
**Create a new population by repeating following steps until the new population is complete**
* Will be left with 10 sequences.

### 4. Selection
**Select two parent chromosomes from a population according to their fitness (the better fitness, the bigger chance to be selected)**
* For remaining sequences, mate in groups of 2.
* #1 pairs with #2, #3 pairs with #4, and so on.

### 5. Crossover
**With a crossover probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents.**
* Split 50% of genes, create 2 children.
  * First child
    * Take the first 10 bits from survivor #1.
      * `00100-10100-10010-00100`
    * Take the last 10 bits from survivor #2.
      * `0001-10101-00010-01101`
    * New sequence!
      * `00100-10100-00010-01101`
  * Second child
    * Take the last 10 bits from survivor #1.
      * `00100-10100-10010-00100`
    * Take the first 10 bits from survivor #2.
      * `0001-10101-00010-01101`
    * New sequence!
      * `00100-10100-00010-01101`

### 6. Mutation
**With a mutation probability mutate new offspring at each locus (position in chromosome).**
  1. Children of #1 and #2 have 5% chance one random bit is flipped
    * first child `00100-10100-00010-01101`
    * `0` `0100-10100-00010-01101` 1st bit mutates
    * `1` `0100-10100-00010-01101`

### 7. Accepting
  **Place new offspring in a new population**
  1. Place all children and parents back into the population.
    * 10 parents
    * 10 children

### 8. Replace
**Use new generated population for a further run of algorithm**
  * Run fitness step

### 9. Test
**If the end condition is satisfied, stop, and return the best solution in current population**
  * if two parents are ever both `11111-11111-11111-11111`, stop the program

### 10. [Loop]
**Go to step 2**



***
***

## Notes on a program idea

## Population
### City X
  * fitness_X = 50
  * city_X numbers = Pick fitness_X amount of random numbers 1–100


### City Y
  * fitness_Y = 50
  * city_Y numbers = Picks fitness_Y amount of random numbers 101-200

## Fitness
### Fitness picker
  * fitness_Z = Pick random number 1–200

### Fitness selection
    for each of city_X numbers:
        if city_X[number] > Z
          fitness_X = fitness_X - 1

    for each of city_Y numbers:
        if city_Y[number] > Z
          fitness_Y = fitness_Y - 1

## Genetic selection
  ???


##
