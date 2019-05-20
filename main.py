from ant_colony import AntColony
from utils.csv_converter import CsvConverter
from tsp import le_coordenadas_tsp, dicio_cidades, distance
from particle_swarm_optimization_permut import ParticleSwarm


def read_solution():
    with open('test_cases/berlin52.opt.tour') as fp:
        solution = fp.readlines()
        solution = list(map(int, solution[4:len(solution) - 1]))
        return solution


# load world
SmallWorld = le_coordenadas_tsp('test_cases/monalisa.tsp')
SmallWorld_sol = read_solution()
dicio = dicio_cidades(SmallWorld)

def eval_solution(distance_callback):
    def total_solution_distance(solution, dicio):
        total_distance = 0
        for i in range(1, len(solution)):
            total_distance += distance_callback(
                dicio[solution[i - 1]], dicio[solution[i]])
        return total_distance

    return total_solution_distance


def main():
    ''' Main function worker '''
    initial = [x for x in range(len(dicio))]
    pso_results = ParticleSwarm(
        eval_solution(distance),
        initial,
        dicio,
        num_particles=50,
        maxiter=80)

    data = {"best_individuals": pso_results.best_individuals,
            "fitness_averages": pso_results.fitness_averages,
            "generation_calculation_times": pso_results.generation_calculation_times,
            "population_initialization_time": pso_results.population_initialization_time}

    print(" ------------------ Converting ---------------------")
    converter = CsvConverter('first_text.csv', data)
    converter.pso_to_csv()


if __name__ == "__main__":
	main()
