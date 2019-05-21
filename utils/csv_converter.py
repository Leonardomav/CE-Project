''' Module to convert data to CSV '''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class CsvConverter():
    """ Converter for algorithm data to CSV """

    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def pso_to_csv(self):
        ''' Convert PSO data to CSV file '''
        csv = open(self.filename, "w")

        population_initialization_title_row = "Population Initialization, Population Size, Iterations, Weight, Cognitive, Social\n"
        csv.write(population_initialization_title_row)
        csv.write(
            str(self.data["population_initialization_time"]) + "," + str(self.data["population_size"]) + "," + str(
                self.data["iterations"]) + "," + str(self.data["weight"]) + "," + str(
                self.data["cognitive"]) + "," + str(self.data["social"]) + "\n")

        data_title_row = "Iteration, Best Individual (Position), Best Individual (Fitness), Fitness Average, Calculation Time\n"
        csv.write(data_title_row)

        generation = 0
        for best_individual, fitness_average, calculation_time in zip(self.data["best_individuals"],
                                                                      self.data["fitness_averages"],
                                                                      self.data["generation_calculation_times"]):
            row = str(generation) + ",\"" + str(best_individual[0]) + "\",\"" + str(best_individual[1]) + "\"," + str(
                fitness_average) + "," + str(calculation_time) + "\n"
            csv.write(row)

            generation += 1

        csv.close()

    def aco_to_csv(self):
        ''' Convert ACO data to CSV file '''
        csv = open(self.filename, "w")

        population_initialization_title_row = "Population Initialization, Population Size, Iterations, Alpha, Beta, Evaporation Coefficient\n"
        csv.write(population_initialization_title_row)
        csv.write(
            str(self.data["population_initialization_time"]) + "," + str(self.data["population_size"]) + "," + str(
                self.data["iterations"]) + "," + str(self.data["alpha"]) + "," + str(self.data["beta"]) + "," + str(
                self.data["evaporation_coeficient"]) + "\n")

        data_title_row = "Iteration, Best Individual (Position), Best Individual (Fitness), Fitness Average, Calculation Time\n"
        csv.write(data_title_row)

        generation = 0
        for best_individual, fitness_average, calculation_time in zip(self.data["best_individuals"],
                                                                      self.data["fitness_averages"],
                                                                      self.data["generation_calculation_times"]):
            row = str(generation) + ",\"" + str(best_individual[0]) + "\",\"" + str(best_individual[1]) + "\"," + str(
                fitness_average) + "," + str(calculation_time) + "\n"
            csv.write(row)
            generation += 1

        csv.close()

    def aco_to_graph(self, path):

        for map in ["large", "medium", "small"]:
            for a in [1, 5]:
                for b in [2.5, 5]:
                    for e in [0.3, 0.6]:
                        BestIndiv = []
                        FitAverage = []
                        BestAverage = []
                        for i in range(30):
                            file = "aco_" + map + "_a_" + str(a) + "_b_" + str(b) + "_e_" + str(e) + "_" + str(
                                i + 1) + ".csv"
                            file_i = path + file
                            df = pd.read_csv(file_i, skiprows=2)
                            df['Best Individual (Fitness)'] = pd.to_numeric(df['Best Individual (Fitness)'])

                            if i == 0:
                                BestAverage.extend(df['Best Individual (Fitness)'].tolist())
                                FitAverage.extend(df['Fitness Average'].tolist())
                                BestIndiv.extend(df['Best Individual (Fitness)'].tolist())

                            else:
                                BestAverageAux = (df['Best Individual (Fitness)'].tolist())
                                BestAverage = [((BestAverage[i] + BestAverageAux[i]) / 2) if i < len(BestAverage) else
                                               BestAverageAux[i]
                                               for i in range(len(BestAverageAux))]

                                FitAverageAux = (df['Fitness Average'].tolist())
                                FitAverage = [
                                    ((FitAverage[i] + FitAverageAux[i]) / 2) if i < len(FitAverage) else FitAverageAux[
                                        i] for
                                    i in range(len(FitAverageAux))]

                                BestIndivAux = (df['Best Individual (Fitness)'].tolist())
                                BestIndiv = [
                                    BestIndivAux[i] if i >= len(BestIndiv) or BestIndivAux[i] < BestIndiv[i] else
                                    BestIndiv[i] for i in range(len(BestIndivAux))]

                        plt.plot(BestIndiv, label='Best Individual (Fitness)')
                        plt.plot(FitAverage, label='Fitness Average')
                        plt.plot(BestAverage, label='Best Average (Fitness)')

                        plt.legend()
                        plt.savefig('./test_results/graphs/aco/' + file + '.png')
                        plt.show()

    def pso_to_graph(self, path):

        for map in ["large", "medium", "small"]:
            for cs in [1, 2, 3]:
                for w in [0.6, 0.9]:
                    BestIndiv = []
                    FitAverage = []
                    BestAverage = []
                    for i in range(30):
                        file = "pso_" + map + "_w_" + str(w) + "_cs_" + str(cs) + "_" + str(i + 1) + ".csv"
                        file_i = path + file
                        df = pd.read_csv(file_i, skiprows=2)
                        df['Best Individual (Fitness)'] = pd.to_numeric(df['Best Individual (Fitness)'])

                        if i == 0:
                            BestAverage.extend(df['Best Individual (Fitness)'].tolist())
                            FitAverage.extend(df['Fitness Average'].tolist())
                            BestIndiv.extend(df['Best Individual (Fitness)'].tolist())

                        else:
                            BestAverageAux = (df['Best Individual (Fitness)'].tolist())
                            BestAverage = [((BestAverage[i] + BestAverageAux[i]) / 2) if i < len(BestAverage) else
                                           BestAverageAux[i]
                                           for i in range(len(BestAverageAux))]
                            FitAverageAux = (df['Fitness Average'].tolist())
                            FitAverage = [
                                ((FitAverage[i] + FitAverageAux[i]) / 2) if i < len(FitAverage) else FitAverageAux[
                                    i] for
                                i in range(len(FitAverageAux))]
                            BestIndivAux = (df['Best Individual (Fitness)'].tolist())
                            BestIndiv = [
                                BestIndivAux[i] if i >= len(BestIndiv) or BestIndivAux[i] < BestIndiv[i] else
                                BestIndiv[i] for i in range(len(BestIndivAux))]

                    plt.plot(BestIndiv, label='Best Individual (Fitness)')
                    plt.plot(FitAverage, label='Fitness Average')
                    plt.plot(BestAverage, label='Best Average (Fitness)')

                    plt.legend()
                    plt.savefig('./test_results/graphs/pso/' + file + '.png')
                    plt.show()
