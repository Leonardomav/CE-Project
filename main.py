import antcolony as aco
from tsp import le_coordenadas_tsp, dicio_cidades, distancia

# load world
SmallWorld = le_coordenadas_tsp('test_cases/berlin52.tsp')
BigWorld = le_coordenadas_tsp('test_cases/world.tsp')
dicio = dicio_cidades(SmallWorld)

# Preforms ACO
colony = aco.AntColony(dicio, distancia)
answer = colony.mainloop()
print("-- FINISHED --")
print(answer)


