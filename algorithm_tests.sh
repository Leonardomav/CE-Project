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
    python3 main.py --pso --filename=test_results/pso_small_pop_${populations[$index]}_$test_index.csv --map 1 -p ${populations[$index]} -i 500  -w 0.6 -c 1 -s 2 
    python3 main.py --pso --filename=test_results/pso_medium_pop_${populations[$index]}_$test_index.csv --map 2 -p ${populations[$index]} -i 500 -w 0.6 -c 1 -s 2 
    python3 main.py --pso --filename=test_results/pso_large_pop_${populations[$index]}_$test_index.csv --map 3 -p ${populations[$index]} -i 500 -w 0.6 -c 1 -s 2 

    python3 main.py --pso --filename=test_results/pso_small_it_${iterations[$index]}_$test_index.csv --map 1 -p 250 -i ${iterations[$index]} -w 0.5 -c 1 -s 2 
    python3 main.py --pso --filename=test_results/pso_medium_it_${iterations[$index]}_$test_index.csv --map 2 -p 250 -i ${iterations[$index]} -w 0.5 -c 1 -s 2 
    python3 main.py --pso --filename=test_results/pso_large_it_${iterations[$index]}_$test_index.csv --map 3 -p 250 -i ${iterations[$index]} -w 0.5 -c 1 -s 2 

    python3 main.py --pso --filename=test_results/pso_small_w_${weights[$index]}_$test_index.csv --map 1 -p 250 -i 500  -w ${weights[$index]} -c 1 -s 2 
    python3 main.py --pso --filename=test_results/pso_medium_w_${weights[$index]}_$test_index.csv --map 2 -p 250 -i 500 -w ${weights[$index]} -c 1 -s 2 
    python3 main.py --pso --filename=test_results/pso_large_w_${weights[$index]}_$test_index.csv --map 3 -p 250 -i 500 -w ${weights[$index]} -c 1 -s 2 

    python3 main.py --pso --filename=test_results/pso_small_cog_${cognitives[$index]}_$test_index.csv --map 1 -p 250 -i 500  -w 0.6 -c ${cognitives[$index]} -s 2 
    python3 main.py --pso --filename=test_results/pso_medium_cog_${cognitives[$index]}_$test_index.csv --map 2 -p 250 -i 500 -w 0.6 -c ${cognitives[$index]} -s 2 
    python3 main.py --pso --filename=test_results/pso_large_cog_${cognitives[$index]}_$test_index.csv --map 3 -p 250 -i 500 -w 0.6 -c ${cognitives[$index]} -s 2 

    python3 main.py --pso --filename=test_results/pso_small_soc_${socials[$index]}_$test_index.csv --map 1 -p 250 -i 500  -w 0.6 -c 1 -s ${socials[$index]} 
    python3 main.py --pso --filename=test_results/pso_medium_soc_${socials[$index]}_$test_index.csv --map 2 -p 250 -i 500 -w 0.6 -c 1 -s ${socials[$index]} 
    python3 main.py --pso --filename=test_results/pso_large_soc_${socials[$index]}_$test_index.csv --map 3 -p 250 -i 500 -w 0.6 -c 1 -s ${socials[$index]} 
  done
done

# ACO Tests

for test_index in {1..30} 
do
  declare -a populations=(100 250 500)
  declare -a iterations=(100 500 1000)
  declare -a alphas=(0.4 0.6 0.9)
  declare -a betas=(0.5 1 2)
  declare -a evaps=(0.5 1 2)

  for index in {1..3}
  do
    python3 main.py --aco --filename=test_results/aco_small_pop_${populations[$index]}_$test_index.csv --map 1 -p ${populations[$index]} -i 500  -a 0.6 -b 1 -pec 2 
    python3 main.py --aco --filename=test_results/aco_medium_pop_${populations[$index]}_$test_index.csv --map 2 -p ${populations[$index]} -i 500 -a 0.6 -b 1 -pec 2 
    python3 main.py --aco --filename=test_results/aco_large_pop_${populations[$index]}_$test_index.csv --map 3 -p ${populations[$index]} -i 500 -a 0.6 -b 1 -pec 2 

    python3 main.py --aco --filename=test_results/aco_small_it_${iterations[$index]}_$test_index.csv --map 1 -p 250 -i ${iterations[$index]} -a 0.5 -b 1 -pec 2 
    python3 main.py --aco --filename=test_results/aco_medium_it_${iterations[$index]}_$test_index.csv --map 2 -p 250 -i ${iterations[$index]} -a 0.5 -b 1 -pec 2 
    python3 main.py --aco --filename=test_results/aco_large_it_${iterations[$index]}_$test_index.csv --map 3 -p 250 -i ${iterations[$index]} -a 0.5 -b 1 -pec 2 

    python3 main.py --aco --filename=test_results/aco_small_a_${alphas[$index]}_$test_index.csv --map 1 -p 250 -i 500  -a ${alphas[$index]} -b 1 -pec 2 
    python3 main.py --aco --filename=test_results/aco_medium_a_${alphas[$index]}_$test_index.csv --map 2 -p 250 -i 500 -a ${alphas[$index]} -b 1 -pec 2 
    python3 main.py --aco --filename=test_results/aco_large_a_${alphas[$index]}_$test_index.csv --map 3 -p 250 -i 500 -a ${alphas[$index]} -b 1 -pec 2 

    python3 main.py --aco --filename=test_results/aco_small_b_${betas[$index]}_$test_index.csv --map 1 -p 250 -i 500  -a 0.6 -b ${betas[$index]} -pec 2 
    python3 main.py --aco --filename=test_results/aco_medium_b_${betas[$index]}_$test_index.csv --map 2 -p 250 -i 500 -a 0.6 -b ${betas[$index]} -pec 2 
    python3 main.py --aco --filename=test_results/aco_large_b_${betas[$index]}_$test_index.csv --map 3 -p 250 -i 500 -a 0.6 -b ${betas[$index]} -pec 2 

    python3 main.py --aco --filename=test_results/aco_small_evap_${evaps[$index]}_$test_index.csv --map 1 -p 250 -i 500  -a 0.6 -b 1 -pec ${evaps[$index]} 
    python3 main.py --aco --filename=test_results/aco_medium_evap_${evaps[$index]}_$test_index.csv --map 2 -p 250 -i 500 -a 0.6 -b 1 -pec ${evaps[$index]} 
    python3 main.py --aco --filename=test_results/aco_large_evap_${evaps[$index]}_$test_index.csv --map 3 -p 250 -i 500 -a 0.6 -b 1 -pec ${evaps[$index]} 
  done
done
