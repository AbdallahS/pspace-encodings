#!/bin/bash

cd solvers
if [ "$2" == "" ]
then
    ./bule $1 ../$2
else
    ./bule $1 ../$2 2>/dev/null | grep "SAT\|UNSAT"
fi
cd ..