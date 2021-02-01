#!/bin/bash

cd ..
for x in graph-instances/*.bul
do
    (time ./test $x problems/vertex-cover.bul) 2>&1 | grep "real\|SAT" >> temp.txt
done
cat temp.txt
rm temp.txt
