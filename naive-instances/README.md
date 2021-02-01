# Naive counter complexity analysis

## Dependencies

The testing is done with matplotlib python library

``` pip install matplotlib```

## Usage

Run from ```naive-instances/``` directory

```./graph.bash```

This will iterate through all ```.bul``` files in current repository and plot the real time against number of verticies into a .png file. 

----------------------------------------------------------------------------------------------------------------

# Note for Sequential (can be deleted later)

Original Sinz Cardinality Constraint for Sequential-counter:

![sinz](https://user-images.githubusercontent.com/65769889/105673913-d3bc3180-5f3a-11eb-99be-6b4b2a46069d.PNG)

Improved Knuth's expression:

![knuth](https://user-images.githubusercontent.com/65769889/105673909-d28b0480-5f3a-11eb-84a0-721b05514062.PNG)

Using Knuth's improved sequential cardinality constraints, vertex cover can be re-expressed.
Let r = budget, n = num. vertex.

### Sources

https://arxiv.org/pdf/1810.12975.pdf

https://www.carstensinz.de/papers/CP-2005.pdf

https://people.smp.uq.edu.au/RadislavVaisman/papers/vertex-cover_STCO.pdf
