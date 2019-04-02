import ant_colony as aco
from tsp import le_coordenadas_tsp, dicio_cidades


teste = le_coordenadas_tsp('/Users/soren/Work/Masters/CE/CE-Projecto/world.tsp')
dicio = dicio_cidades(teste)
def distance(start, end):
	x_distance = abs(start[0] - end[0])
	y_distance = abs(start[1] - end[1])
	
	import math
	return math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))

colony = aco.ant_colony(dicio, distance)

answer = colony.mainloop()
print(answer)
