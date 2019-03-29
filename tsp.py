"""
tsp_2017.py
Ernesto Costa, February 2017
"""
import os
from sea_perm import *
from utils import *
from math import sqrt

# interface
# from file to coordinates

def le_coordenadas_tsp(ficheiro):
    """ From a TSP format file return the matrix of coordinates."""
    with  open(ficheiro) as fich_in:
	# read header
        linha = fich_in.readline()
        while not linha.split()[0].isdigit():
            linha = fich_in.readline()
        # read coordinates
        n, x, y = linha.split()
        coordenadas = [(float(x), float(y))]
        resto = fich_in.readlines()
        for linha in resto[:-1]:
            n, x, y = linha.split()
            coordenadas.append((float(x), float(y)))
    return coordenadas

# from coordinates to dictionary
def dicio_cidades(coordenadas):
    """ Create a dictionary with the cities and their coordinates."""
    dicio = {}
    for i, (x, y) in enumerate(coordenadas):
        dicio[i] = (x, y)
    return dicio

# fitness
def merito(dicio_cidades):
    def merito_(indiv):
        return evaluate(fenotipo(indiv,dicio_cidades))
    return merito_

def fenotipo(genotipo,dicio_cidades):
    """ Return ther phenotype."""
    fen = [dicio_cidades[cidade] for cidade in genotipo]
    return fen

def evaluate(caminho):
    num_cidades = len(caminho)
    comp = 0
    for i in range(num_cidades):
        j = (i + 1) % num_cidades
        comp += distancia(caminho[i], caminho[j])
    return comp

def distancia(cid_i, cid_j):
    """ Euclidian distance."""
    x_i, y_i = cid_i
    x_j, y_j = cid_j
    dx = x_i - x_j
    dy = y_i - y_j
    dist = sqrt(dx ** 2 + dy ** 2)
    return dist

if __name__ == '__main__':
    """This is for my use. You should adapt to your situation!!!"""
    #filepath = '/Users/ernestojfcosta/data/'
    filepath = os.getcwd()
    coord = le_coordenadas_tsp(filepath+'/berlin52.tsp')
    dicio = dicio_cidades(coord)
    #print(dicio)
    meu_merito = merito(dicio)
    size_cromo = len(dicio)
    #best = sea_perm(30,20, size_cromo, 0.1,  0.8,tour_sel(3),order_cross,muta_cromo,sel_survivors_elite(0.1), meu_merito)
    #print(best)
    
    #best, stat, stat_average = sea_perm_for_plot(30,20, size_cromo, 0.1,  0.8,tour_sel(3),order_cross,muta_cromo,sel_survivors_elite(0.1), meu_merito)
    #display_stat_1(stat,stat_average)  
    
    
    boa, best_average = run(5,30,20, size_cromo, 0.1,  0.8,tour_sel(3),order_cross,muta_cromo,sel_survivors_elite(0.1), meu_merito)
    display_stat_n(boa,best_average)      
    
