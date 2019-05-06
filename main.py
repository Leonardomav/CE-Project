from ant_colony import AntColony
from tsp import le_coordenadas_tsp, dicio_cidades, distance
from particle_swarm_optimization_permut import ParticleSwarm

# load world
SmallWorld = le_coordenadas_tsp('test_cases/berlin52.tsp')
BigWorld = le_coordenadas_tsp('test_cases/world.tsp')
dicio = dicio_cidades(SmallWorld)

def eval_solution(distance_callback):
	def total_solution_distance(solution, dicio):
		total_distance = 0
		for i in range(1, len(solution)):
			total_distance += distance_callback(dicio[solution[i - 1]], dicio[solution[i]])
		return total_distance
	return total_solution_distance

initial = [ x for x in range(len(dicio))]
ParticleSwarm(eval_solution(distance),initial, dicio, num_particles=50,maxiter=80)
colony = aco.AntColony(dicio, distance)

answer = colony.mainloop()
print("-- FINISHED --")
print(answer)
print(eval_solution(distance)(answer, dicio))

