#!/bin/bash

# For simplicity, only allow max 3 arguments
cd solvers
if [ "$2" == "" ]
then
    ./bule $1 ../$2
else
    if [ "$3" == "-g" ]
    then 
        echo -e "\n---------- Solver Output -----------\n"
        ./main ground -t=1 -u=0 ../$2 2> /dev/null | grep -v '%% Rules:'
        echo -e "\n---------- Result Output -----------\n"
        ./bule $1 ../$2 2>/dev/null | grep "SAT\|UNSAT"
        echo ""
    elif [ "$3" == "" ]
    then 
        echo -e "\n---------- Result Output -----------\n"
        ./bule $1 ../$2 2>/dev/null | grep "SAT\|UNSAT"
        echo ""
    else  
        echo "Usage: ./bule.sh command [filename] [-g]"
    fi
fi
cd ..