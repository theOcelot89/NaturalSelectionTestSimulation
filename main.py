# Import required modules
from random import sample, choice
import matplotlib.pyplot as plt


# Define environment class
class Environment:
    def __init__(self, size=1000, food_density=0.01, n=1):
        self.n = n
        self.size = size
        self.x = range(0, size)

        self.food_density = food_density
        self.foodPos = sample(self.x, int(size * food_density))
        self.population = self.createPopulation()


    def createPopulation(self):
        population = [Organism(self) for x in range(self.n)]
        return population

    def getOrgPositions(self):
        orgPositions = [x.pos for x in self.population]
        return orgPositions

    def plotEnvironment(self):
        fig, ax = plt.subplots()

        #plot the food
        ax.plot(self.foodPos, self.foodPos, 'go')

        #plot the organisms
        orgPositions = self.getOrgPositions()
        ax.plot(self.getOrgPositions(), self.getOrgPositions(), 'ro')
        plt.show()

# Define organisms class
class Organism:
    def __init__(self, env, parent=None):
        self.env = env
        self.food = 0
        self.pos = choice(self.env.x)
        self.speed = 1
        self.direction = choice([1, -1])


env = Environment(n=10)
env.plotEnvironment()
