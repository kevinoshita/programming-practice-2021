def exercise_4(inputs): # DO NOT CHANGE THIS LINE
    
    import numpy as np
    import matplotlib.pyplot as plt

    def mutation(pop, number_of_individuals, F):
        index1 = np.random.randint(number_of_individuals)
        index2 = np.random.randint(number_of_individuals)
        index3 = np.random.randint(number_of_individuals)
        print(index1)
        print(index2)
        print(index3)
        print(pop[index1])
        print(pop[index2])
        print(pop[index3])
        mut_vector = (pop[index1] - pop[index2])*F + pop[index3]
        return mut_vector

    def crossover(father, mut_vector, number_of_variables):
        child = [father[i] if np.random.rand() < 0.8 else mut_vector[i] for i in range(number_of_variables)]
        print(child)
        return child
    def evaluation_sphere(variables):
        #Sphere
        return -np.sum(np.square(variables))

    def evaluation_dixonprice(variables):
        #DixonPrice
        return (variables[0]-1)**2 + sum((i+1)*(2*variables[i]**2-variables[i-1])**2 for i in range(1, len(variables)))

    class DE:

        #self.generations= 1000

        def __init__(self, number_of_variables, number_of_individuals, F):
            self.number_of_variables = number_of_variables
            self.number_of_individuals = number_of_individuals
            self.pop = np.random.rand(number_of_individuals, number_of_variables)
            self.F = F
            self.generations = 1000
            #print(type(self.pop))

        def optimize(self):
            graph = []
            for gen in range(self.generations):
                pop_eval = []
                for index,individual in enumerate(self.pop):
                    mut_vector = mutation(self.pop, self.number_of_individuals, self.F)
                    child = crossover(individual, mut_vector, self.number_of_variables)

                    if evaluation_dixonprice(child) > evaluation_dixonprice(individual):
                        self.pop[index] = child

                    pop_eval.append(evaluation_dixonprice(self.pop[index]))

                avg_evaluation = np.mean(pop_eval)
                print(avg_evaluation)

                graph.append(avg_evaluation)
                plt.plot(graph)
                plt.draw()
                plt.pause(0.0001)
                plt.clf()

    F = 1.0
    number_of_variables = 2
    number_of_individuals = 100
    de = DE(number_of_variables, number_of_individuals, F)
    de.optimize()
        output = inputs

    return output       # DO NOT CHANGE THIS LINE
