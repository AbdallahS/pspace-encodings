# pspace-encodings

## Usage

### Test files for satisfiability
To concatenate and test a problem and input file, run 

```./test file_name1 file_name2```

For example, 

```./test graph-instances/graph1.bul problems/vertex-cover.bul```

This will concatenate the given files and run it under bule to solve the instance and return either SAT or UNSAT.

### Flags

Add either of the following flags to show grounded and/or file output:

``` -f / --file => display concatenated file content to standard output ```

``` -g / --ground => display grounded output of bule encoding to standard output ```

### Examples

* ```./test graph-instances/graph1.bul problems/vertex-cover.bul```

will give

```
---------- Result Output -----------

s SAT
```

* ```./test graph-instances/graph1.bul problems/vertex-cover.bul -f -g```
 
 will give
 ```
 ----------- File Output ------------

vertex[1..5].
edge[1,2]. edge[1,3]. edge[1,4]. edge[1,5].
edge[2,3]. edge[2,4]. edge[2,5].
edge[3,4]. edge[3,5].
edge[4,5].

% Rule for budget constraints (budget = 4)
vertex[V1], vertex[V2], vertex[V3], vertex[V4], vertex[V5],
    V1 < V2, V2 < V3, V3 < V4, V4 < V5 ::
    ~s(V1), ~s(V2), ~s(V3), ~s(V4), ~s(V5).

%%% covering edges
edge[U, V] :: s(U), s(V).

---------- Solver Output -----------

~s(1), ~s(2), ~s(3), ~s(4), ~s(5).
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

---------- Result Output -----------

s SAT
```

## Budget generator for vertex cover

The ```budget``` file located in ```graph-instances``` allows easy constuction of budget constraint in bule (for naive encodings).

To execute, change current directory to ```graph-instances``` and run

```./budget budget_requirement```

For example, 

```./budget 4```

will output

```
% Rule for budget constraints (budget = 4)
vertex[V1], vertex[V2], vertex[V3], vertex[V4], vertex[V5],
    V1 < V2, V2 < V3, V3 < V4, V4 < V5 ::
    ~s(V1), ~s(V2), ~s(V3), ~s(V4), ~s(V5).
```

which can be manually copy-pasted into input files.

## Attributions

Bule binary from:  https://github.com/vale1410/bule

Depqbf QBF solver binary from: http://lonsing.github.io/depqbf/

Kissat SAT solver binary from: http://fmv.jku.at/kissat/
