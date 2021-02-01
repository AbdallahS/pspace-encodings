#!/bin/bash

cd ..
for x in graph-instances/* 
do
    time echo ""
    (time ./test $x problems/vertex-cover.bul)
    (time ./test $x problems/vertex-cover.bul) 2>&1 | grep "real" >> temp.txt
done
cat temp.txt
rm temp.txt
