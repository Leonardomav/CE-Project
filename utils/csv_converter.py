''' Module to convert data to CSV '''

from pprint import pprint

class CsvConverter():
    ''' Converter for algorithm data to CSV '''

    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def pso_to_csv(self):
        ''' Convert PSO data to CSV file '''
        csv = open(self.filename, "w")

        population_initialization_title_row = "Population Initialization, Population Size, Iterations, Weight, Cognitive, Social\n"
        csv.write(population_initialization_title_row)
        csv.write(str(self.data["population_initialization_time"])+ "," + str(self.data["population_size"]) + "," + str(self.data["iterations"]) + "," + str(self.data["weight"]) + "," + str(self.data["cognitive"]) + "," + str(self.data["social"]) + "\n")

        data_title_row = "Iteration, Best Individual (Position), Best Individual (Fitness), Fitness Average, Calculation Time\n"
        csv.write(data_title_row)

        generation = 0
        for best_individual, fitness_average, calculation_time in zip(self.data["best_individuals"], self.data["fitness_averages"], self.data["generation_calculation_times"]):
            row = str(generation) + ",\"" + str(best_individual[0]) + "\",\"" + str(best_individual[1]) + "\"," + str(fitness_average) + "," + str(calculation_time) + "\n"
            csv.write(row)
            generation+=1

        csv.close()

    def aco_to_csv(self):
        ''' Convert ACO data to CSV file '''
        csv = open(self.filename, "w")

        population_initialization_title_row = "Population Initialization, Population Size, Iterations, Alpha, Beta, Evaporation Coefficient\n"
        csv.write(population_initialization_title_row)
        csv.write(str(self.data["population_initialization_time"])+ "," + str(self.data["population_size"]) + "," + str(self.data["iterations"]) + "," + str(self.data["alpha"]) + "," + str(self.data["beta"]) + "," + str(self.data["evaporation_coeficient"]) + "\n")

        data_title_row = "Iteration, Best Individual (Position), Best Individual (Fitness), Fitness Average, Calculation Time\n"
        csv.write(data_title_row)

        generation = 0
        for best_individual, fitness_average, calculation_time in zip(self.data["best_individuals"], self.data["fitness_averages"], self.data["generation_calculation_times"]):
            row = str(generation) + ",\"" + str(best_individual[0]) + "\",\"" + str(best_individual[1]) + "\"," + str(fitness_average) + "," + str(calculation_time) + "\n"
            csv.write(row)
            generation+=1

        csv.close()
