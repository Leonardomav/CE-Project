#!/bin/bash

# PSO Tests

for test_index in {1..30} 
do
  declare -a populations=(100 250 500)
  declare -a iterations=(100 500 1000)
  declare -a weights=(0.4 0.6 0.9)
  declare -a cognitives=(0.5 1 2)
  declare -a socials=(0.5 1 2)

  for index in {1..3}
  do
    python3 main.py --pso --filename=test_results/pso_small_pop_${populations[$index]}_$test_index.csv --map 1 -p ${populations[$index]} -i 500  -w 0.6 -c 1 -s 2 # Small map
    python3 main.py --pso --filename=test_results/pso_medium_pop_${populations[$index]}_$test_index.csv --map 2 -p ${populations[$index]} -i 500 -w 0.6 -c 1 -s 2 # Medium map
    python3 main.py --pso --filename=test_results/pso_large_pop_${populations[$index]}_$test_index.csv --map 3 -p ${populations[$index]} -i 500 -w 0.6 -c 1 -s 2 # Large map

    python3 main.py --pso --filename=test_results/pso_small_it_${iterations[$index]}_$test_index.csv --map 1 -p 250 -i ${iterations[$index]} -w 0.5 -c 1 -s 2 # Small map
    python3 main.py --pso --filename=test_results/pso_medium_it_${iterations[$index]}_$test_index.csv --map 2 -p 250 -i ${iterations[$index]} -w 0.5 -c 1 -s 2 # Medium map
    python3 main.py --pso --filename=test_results/pso_large_it_${iterations[$index]}_$test_index.csv --map 3 -p 250 -i ${iterations[$index]} -w 0.5 -c 1 -s 2 # Large map

    python3 main.py --pso --filename=test_results/pso_small_w_${weights[$index]}_$test_index.csv --map 1 -p 250 -i 500  -w ${weights[$index]} -c 1 -s 2 # Small map
    python3 main.py --pso --filename=test_results/pso_medium_w_${weights[$index]}_$test_index.csv --map 2 -p 250 -i 500 -w ${weights[$index]} -c 1 -s 2 # Medium map
    python3 main.py --pso --filename=test_results/pso_large_w_${weights[$index]}_$test_index.csv --map 3 -p 250 -i 500 -w ${weights[$index]} -c 1 -s 2 # Large map

    python3 main.py --pso --filename=test_results/pso_small_cog_${cognitives[$index]}_$test_index.csv --map 1 -p 250 -i 500  -w 0.6 -c ${cognitives[$index]} -s 2 # Small map
    python3 main.py --pso --filename=test_results/pso_medium_cog_${cognitives[$index]}_$test_index.csv --map 2 -p 250 -i 500 -w 0.6 -c ${cognitives[$index]} -s 2 # Medium map
    python3 main.py --pso --filename=test_results/pso_large_cog_${cognitives[$index]}_$test_index.csv --map 3 -p 250 -i 500 -w 0.6 -c ${cognitives[$index]} -s 2 # Large map

    python3 main.py --pso --filename=test_results/pso_small_soc_${social[$index]}_$test_index.csv --map 1 -p 250 -i 500  -w 0.6 -c 1 -s ${socials[$index]} # Small map
    python3 main.py --pso --filename=test_results/pso_medium_soc_${social[$index]}_$test_index.csv --map 2 -p 250 -i 500 -w 0.6 -c 1 -s ${socials[$index]} # Medium map
    python3 main.py --pso --filename=test_results/pso_large_soc_${social[$index]}_$test_index.csv --map 3 -p 250 -i 500 -w 0.6 -c 1 -s ${socials[$index]} # Large map
  done
done

# ACO Tests

# for test_index in {1..30} 
# do
#   python3 main.py --aco --filename=test_results/aco_small_$test_index.csv --map 1 -p 50 -i 100 -a 0.5 -b 1.2 -pec 0.4 # Small map
#   python3 main.py --aco --filename=test_results/aco_medium_$test_index.csv --map 2 -p 50 -i 100 -a 0.5 -b 1.2 -pec 0.4 # Medium map
#   python3 main.py --aco --filename=test_results/aco_large_$test_index.csv --map 3 -p 50 -i 100 -a 0.5 -b 1.2 -pec 0.4 # Large map
# done
