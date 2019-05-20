#!/bin/bash

# PSO Tests

for test_index in {1..30} 
do
  declare -a populations=(50 100 150 200 300 500)
  declare -a weights=(0.25 0.5 0.6 0.7 0.8 0.9)
  declare -a cognitives=(0.5 1 2)
  declare -a socials=(0.5 1 2)

  for iteration in $(seq 100 500 100) 
  do
    python3 main.py --pso --filename=test_results/pso_small_$test_index.csv --map 1 -p 50 -i $iteration -w 0.5 -c 1 -s 2 # Small map
    python3 main.py --pso --filename=test_results/pso_medium_$test_index.csv --map 2 -p 50 -i $iteration -w 0.5 -c 1 -s 2 # Medium map
    python3 main.py --pso --filename=test_results/pso_large_$test_index.csv --map 3 -p 50 -i $iteration -w 0.5 -c 1 -s 2 # Large map
  done
  
  for population in {1..6}
  do
  done

  for index in {1..5}
  do
    python3 main.py --pso --filename=test_results/pso_small_$test_index.csv --map 1 -p 50 -i $iteration -w ${weights[$index]} -c 1 -s 2 # Small map
    python3 main.py --pso --filename=test_results/pso_medium_$test_index.csv --map 2 -p 50 -i $iteration -w ${weights[$index]} -c 1 -s 2 # Medium map
    python3 main.py --pso --filename=test_results/pso_large_$test_index.csv --map 3 -p 50 -i $iteraition -w ${weights[$index]} -c 1 -s 2 # Large map
  done

  for index in {1..3}
  do
    python3 main.py --pso --filename=test_results/pso_small_$test_index.csv --map 1 -p 50 -i $iteration -w 0.5 -c ${cognitives[$index]} -s 2 # Small map
    python3 main.py --pso --filename=test_results/pso_medium_$test_index.csv --map 2 -p 50 -i $iteration -w 0.5 -c ${cognitives[$index]} -s 2 # Medium map
    python3 main.py --pso --filename=test_results/pso_large_$test_index.csv --map 3 -p 50 -i $iteraition -w 0.5 -c ${cognitives[$index]} -s 2 # Large map

    python3 main.py --pso --filename=test_results/pso_small_$test_index.csv --map 1 -p 50 -i $iteration -w 0.5 -c 1 -s 2 # Small map
    python3 main.py --pso --filename=test_results/pso_medium_$test_index.csv --map 2 -p 50 -i $iteration -w 0.5 -c 1 -s 2 # Medium map
    python3 main.py --pso --filename=test_results/pso_large_$test_index.csv --map 3 -p 50 -i $iteraition -w 0.5 -c 1 -s 2 # Large map
  done

done

# ACO Tests

# for test_index in {1..30} 
# do
#   python3 main.py --aco --filename=test_results/aco_small_$test_index.csv --map 1 -p 50 -i 100 -a 0.5 -b 1.2 -pec 0.4 # Small map
#   python3 main.py --aco --filename=test_results/aco_medium_$test_index.csv --map 2 -p 50 -i 100 -a 0.5 -b 1.2 -pec 0.4 # Medium map
#   python3 main.py --aco --filename=test_results/aco_large_$test_index.csv --map 3 -p 50 -i 100 -a 0.5 -b 1.2 -pec 0.4 # Large map
# done
