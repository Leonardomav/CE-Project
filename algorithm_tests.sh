#!/bin/bash

# PSO Tests

for test_index in {1..30} 
do
  python3 main.py --pso --filename=test_results/pso_small_$test_index.csv --map 1 -p 50 -g 100 -w 0.5 -c 1 -s 2 # Small map
  python3 main.py --pso --filename=test_results/pso_medium_$test_index.csv --map 2 -p 50 -g 100 -w 0.5 -c 1 -s 2 # Medium map
  python3 main.py --pso --filename=test_results/pso_large_$test_index.csv --map 3 -p 50 -g 100 -w 0.5 -c 1 -s 2 # Large map
done

for test_index in {1..30} 
do
  python3 main.py --aco --filename=test_results/aco_small_$test_index.csv --map 1 -p 50 -g 100 -a 0.5 -b 1.2 -pec 0.4 # Small map
  python3 main.py --aco --filename=test_results/aco_medium_$test_index.csv --map 2 -p 50 -g 100 -a 0.5 -b 1.2 -pec 0.4 # Medium map
  python3 main.py --aco --filename=test_results/aco_large_$test_index.csv --map 3 -p 50 -g 100 -a 0.5 -b 1.2 -pec 0.4 # Large map
done
