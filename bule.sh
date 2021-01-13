#!/bin/bash

cd solvers
./bule $1 ../$2 2>/dev/null | grep "SAT\|UNSAT"
cd ..