#!/bin/bash

echo "Creating Results Graph..."
cd ..
for x in graph-instances/*.bul
do
    (time ./test $x problems/vertex-cover.bul) 2>&1 | grep "real\|SAT" >> graph-instances/temp.txt
    cat $x | grep "# Vertex" >> graph-instances/temp.txt
done
python3 graph-instances/plot.py graph-instances/temp.txt
rm graph-instances/temp.txt
