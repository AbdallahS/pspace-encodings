# pspace-encodings

## Requirements
To run files in this repository, bash and python3 interpreter is required.

## Usage

### Creating bule encodings
To create a new encoding in Bule, execute the ```generate_file.py``` file:

```python3 generate_file.py```

Then, follow the command line instructions carefully. 

### Testing 
To test created Bule files for boolean satisfiability, run

```./bule.sh solve path_to_file```

(Bule.sh is a shell script that returns modified output from original bule binary located in ```solvers``` directory.)
Add an optional ```-g``` flag at <ins>the end of command</ins> to additionally show grounded output. E.g.

```./bule.sh solve vertex-cover/graph1.bul -g```

will produce

```
---------- Solver Output -----------

s(1), s(2).
s(1), s(3).
s(1), s(4).
s(1), s(5).
s(2), s(3).
s(2), s(4).
s(2), s(5).
s(3), s(4).
s(3), s(5).
s(4), s(5).
~s(1), ~s(2), ~s(3), ~s(4).
~s(1), ~s(2), ~s(3), ~s(5).
~s(1), ~s(2), ~s(4), ~s(5).
~s(1), ~s(3), ~s(4), ~s(5).
~s(2), ~s(3), ~s(4), ~s(5).

---------- Result Output -----------

s UNSAT
```

# Useful commands

Other commands include:

```./bule.sh list``` - list installed solver instances (default depqbf and kissat)

```./bule.sh version``` - show bule version (located inside solvers directory)

All other bule commands do not work with bule.sh. To use advanced commands, use the original bule binary in ```solvers/``` directory.
Flags other than ```-g``` are not supported with bule.sh 

## Versions
As of current, the file generator can only create bule encodings for sudoku and naive vertex cover problems.

## Attributions

Bule binary from:  https://github.com/vale1410/bule

Depqbf QBF solver binary from: http://lonsing.github.io/depqbf/

Kissat SAT solver binary from: http://fmv.jku.at/kissat/
