import argparse

from ant_colony import AntColony
from utils.csv_converter import CsvConverter
from tsp import le_coordenadas_tsp, dicio_cidades, distance
from particle_swarm_optimization_permut import ParticleSwarm


def read_solution():
    with open("test_cases/berlin52.opt.tour") as fp:
        solution = fp.readlines()
        solution = list(map(int, solution[4:len(solution) - 1]))
        solution = [x - 1 for x in solution]
        return solution


def eval_solution(distance_callback, dicio):
    def total_solution_distance(solution, dicio):
        total_distance = 0
        for i in range(1, len(solution)):
            total_distance += distance_callback(
                dicio[solution[i - 1]], dicio[solution[i]])
        return total_distance

    def evaluate(solution, dicio):
        num_cidades = len(solution)
        comp = 0
        for i in range(num_cidades):
            j = (i + 1) % num_cidades
            comp += distance_callback(dicio[solution[i]], dicio[solution[j]])
        return comp

    return evaluate


def run_pso(filename, map_param, num_particles,
            maxiter, weight, cognitive, social):
    """ PSO Worker """
    if map_param is 1:
        small_world = le_coordenadas_tsp("test_cases/berlin52.tsp")
        small_world_solution = read_solution()
        dicio = dicio_cidades(small_world)
    elif map_param is 2:
        medium_world = le_coordenadas_tsp("test_cases/kroA100.tsp")
        medium_world_solution = read_solution()
        dicio = dicio_cidades(medium_world)
    elif map_param is 3:
        large_world = le_coordenadas_tsp("test_cases/ch150.tsp")
        large_world_solution = read_solution()
        dicio = dicio_cidades(large_world)

    initial = [x for x in range(len(dicio))]
    pso_results = ParticleSwarm(
        eval_solution(distance, dicio),
        initial,
        dicio,
        num_particles,
        maxiter,
        weight,
        cognitive,
        social)

    data = {"best_individuals": pso_results.best_individuals,
            "fitness_averages": pso_results.fitness_averages,
            "generation_calculation_times": pso_results.generation_calculation_times,
            "population_initialization_time": pso_results.population_initialization_time,
            "population_size": num_particles,
            "iterations": maxiter,
            "weight": weight,
            "cognitive": cognitive,
            "social": social}

    print(" ------------------ Converting ---------------------")
    converter = CsvConverter(filename, data)
    converter.pso_to_csv()
    print(" ------------------ Ending PSO ---------------------")


def run_aco(filename, map_param, num_ants, maxiter,
            alpha, beta, evaporation_coeficient):
    if map_param is 1:
        small_world = le_coordenadas_tsp("test_cases/berlin52.tsp")
        small_world_solution = read_solution()
        dicio = dicio_cidades(small_world)
    elif map_param is 2:
        medium_world = le_coordenadas_tsp("test_cases/kroA100.tsp")
        medium_world_solution = read_solution()
        dicio = dicio_cidades(medium_world)
    elif map_param is 3:
        large_world = le_coordenadas_tsp("test_cases/ch150.tsp")
        large_world_solution = read_solution()
        dicio = dicio_cidades(large_world)

    sol = [0, 21, 48, 31, 17, 30, 20, 16, 2, 44, 18, 40, 7, 8, 9, 42, 32, 50, 10, 51, 13, 12, 46, 25, 26, 27, 11, 24, 3,
           47, 23, 5, 4, 14, 37, 39, 36, 38, 35, 34, 33, 43, 45, 15, 28, 49, 19, 22, 29, 41, 6, 1]
    f = eval_solution(distance, dicio)
    print(f(sol, dicio))

    colony = AntColony(
        dicio,
        distance,
        ant_count=num_ants,
        alpha=alpha,
        beta=beta,
        pheromone_evaporation_coefficient=evaporation_coeficient,
        time_budget=maxiter)
    colony.mainloop()

    data = {"best_individuals": colony.best_individuals,
            "fitness_averages": colony.fitness_averages,
            "generation_calculation_times": colony.generation_calculation_times,
            "population_initialization_time": colony.population_initialization_time,
            "population_size": num_ants,
            "iterations": maxiter,
            "alpha": alpha,
            "beta": beta,
            "evaporation_coeficient": evaporation_coeficient}
    print(" ------------------ Converting ---------------------")
    converter = CsvConverter(filename, data)
    converter.aco_to_csv()
    print(" ------------------ Ending ACO ---------------------")


def main():
    """ Main function worker """
    parser = argparse.ArgumentParser(
        description="Evolutionary Computing project. Ant Colony Optimization and Particle Swarm Optimization implementations for Travelling Salesperson Problem.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--pso",
        help="Use Particle Swarm Optimization",
        dest="pso",
        action="store_true",
        default=False)
    group.add_argument(
        "--aco",
        help="Use Ant Colony Optimization",
        dest="aco",
        action="store_true",
        default=False)
    parser.add_argument(
        "-f",
        "--filename",
        help="File to store results",
        dest="file")
    parser.add_argument(
        "-p",
        "--initial-population",
        help="Inital Population",
        dest="population")
    parser.add_argument(
        "-i",
        "--number-iterations",
        help="Number of Iterations",
        dest="iterations")
    parser.add_argument("-m", "--map", help="Map to run", dest="map")

    # PSO Params
    parser.add_argument(
        "-w",
        "--weight",
        help="PSO: Weight Param",
        dest="weight")
    parser.add_argument(
        "-c",
        "--cognitive",
        help="PSO: Cognitive Param",
        dest="cognitive")
    parser.add_argument(
        "-s",
        "--social",
        help="PSO: Social Param",
        dest="social")

    # ACO Params
    parser.add_argument(
        "-a",
        "--alpha",
        help="ACO: Alpha Param",
        dest="alpha")

    parser.add_argument(
        "-b",
        "--beta",
        help="ACO: Beta Param",
        dest="beta")

    parser.add_argument(
        "-pec",
        "--evaporation-coeficient",
        help="ACO: Pheromone Evaporation Coeficient",
        dest="evaporation_coeficient")

    args = parser.parse_args()

    if args.aco == False and args.pso == False:
        print("DEBUGGING")
        run_pso('a.csv', 1, 10, 10, 0.5, 1, 2)
    if args.file is None:
        print("No storage file provided")
    elif args.population is None:
        print("Lacking initial population value")
    elif args.iterations is None:
        print("Lacking number of iterations value")
    elif args.map is None:
        print("Lacking map to test")
    elif args.pso:
        if args.weight is None or args.cognitive is None or args.social is None:
            print("Lacking algorithm params. Call --help")
        else:
            run_pso(
                args.file, int(
                    args.map), int(
                    args.population), int(
                    args.iterations), float(
                    args.weight), float(
                    args.cognitive), float(
                    args.social))
    elif args.aco:
        if args.alpha is None or args.beta is None or args.evaporation_coeficient is None:
            print("Lacking algorithm params. Call --help")
        else:
            run_aco(
                args.file, int(
                    args.map), int(
                    args.population), int(
                    args.iterations), float(
                    args.alpha), float(
                    args.beta), float(
                    args.evaporation_coeficient))
    else:
        print("No args given. Call --help")


if __name__ == "__main__":
    #filename = "test_results/so_medium_w_0.6_cs_1_1.csv"
    converter = CsvConverter(filename=None, data=None)
    converter.pso_to_graph(path="./test_results/")

    #main()
