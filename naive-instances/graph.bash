#!/bin/bash

echo "Creating Results Graph..."
cd ..
for x in naive-instances/*.bul
do
    (time ./test $x problems/vertex-cover.bul) 2>&1 | grep "real\|SAT\|UNSAT" >> naive-instances/temp.txt
    cat $x | grep "# Vertex" >> naive-instances/temp.txt
done
python3 naive-instances/plot.py naive-instances/temp.txt
rm naive-instances/temp.txt
