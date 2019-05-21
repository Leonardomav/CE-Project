#!/bin/bash

# PSO Tests

for test_index in {1..30} 
do
  declare -a weights=(0.6 0.9)
  declare -a cognitives=(1 2 3)
  declare -a socials=(3 2 1)

  for index_w in {0..1}
  do
    for index_cs in {0..2}
    do
      python3 main.py --pso --filename=test_results/pso_small_w_${weights[$index_w]}_cs_${cognitives[$index_cs]}_$test_index_.csv --map 1 -p 100 -i 15  -w ${weights[$index_w]} -c ${cognitives[$index_cs]} -s ${socials[${index_cs}]}
      # python3 main.py --pso --filename=test_results/pso_medium_w_${weights[$index_w]}_cs_${cognitives[$index_cs]}_$test_index.csv --map 2 -p 100 -i 30 -w ${weights[$index_w]} -c ${cognitives[$index_cs]} -s ${socials[${index_cs}]}
      # python3 main.py --pso --filename=test_results/pso_large_w_${weights[$index_w]}_cs_${cognitives[$index_cs]}_$test_index.csv --map 3 -p 100 -i 45 -w ${weights[$index_w]} -c ${cognitives[$index_cs]} -s ${socials[${index_cs}]}
    done
  done
done

# ACO Tests

# for test_index in {1..30} 
# do
#   declare -a alphas=(1 5)
#   declare -a betas=(2.5 5)
#   declare -a evaps=(0.3 0.6)
# 
#   for index_a in {0..1}
#   do
#     for index_b in {0..1}
#     do
#       for index_e in {0..1}
#       do
#         python3 main.py --aco --filename=test_results/aco_small_a_${alphas[$index_a]}_b_${betas[$index_b]}_e_${evaps[$index_e]}_$test_index.csv --map 1 -p 100 -i 15 -a ${alphas[$index_a]} -b ${betas[index_b]} -pec ${evaps[$index_e]}
#         python3 main.py --aco --filename=test_results/aco_medium_a_${alphas[$index_a]}_b_${betas[$index_b]}_e_${evaps[$index_e]}_$test_index.csv --map 2 -p 100 -i 30 -a ${alphas[$index_a]} -b ${betas[index_b]} -pec ${evaps[$index_e]}
#         python3 main.py --aco --filename=test_results/aco_large_a_${alphas[$index_a]}_b_${betas[$index_b]}_e_${evaps[$index_e]}_$test_index.csv --map 3 -p 100 -i 45 -a ${alphas[$index_a]} -b ${betas[index_b]} -pec ${evaps[$index_e]}
# 
#       done
#     done
#   done
# done
