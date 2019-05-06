import ant_colony as aco
from tsp import le_coordenadas_tsp, dicio_cidades
from particle_swarm_optimization_permut import PSO


teste = le_coordenadas_tsp('/Users/soren/Work/Masters/CE/CE-Projecto/test_cases/berlin52.tsp')
dicio = dicio_cidades(teste)
def distance(start, end):
	x_distance = abs(start[0] - end[0])
	y_distance = abs(start[1] - end[1])
	
	import math
	return math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))

def eval_solution(distance_callback):
	def total_solution_distance(solution, dicio):
		total_distance = 0
		for i in range(1, len(solution)):
			total_distance += distance_callback(dicio[solution[i - 1]], dicio[solution[i]])
		return total_distance
	return total_solution_distance

initial = [ x for x in range(len(dicio))]
PSO(eval_solution(distance),initial, dicio, num_particles=50,maxiter=80)
colony = aco.ant_colony(dicio, distance)

answer = colony.mainloop()
print(answer)
print(eval_solution(distance)(answer, dicio))

