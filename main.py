import antcolony as aco
from tsp import le_coordenadas_tsp, dicio_cidades, distancia

def read_solution():
    with open('test_cases/berlin52.opt.tour') as fp:
        solution = fp.readlines()
        solution = list(map(int,solution[4:len(solution)-1]))
        return solution

# load world
SmallWorld = le_coordenadas_tsp('test_cases/berlin52.tsp')
SmallWorld_sol = read_solution()
dicio = dicio_cidades(SmallWorld)

# Preforms ACO
colony = aco.AntColony(dicio, distancia)
answer = colony.mainloop()
print("-- FINISHED --")
print(answer)


