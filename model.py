import random
import operator
import matplotlib.pyplot as plt
import agentframework
import csv

num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20



""" adding anew variable neighbourhood """

    
def distance_between(a, b):
    """ Calculated the distance between a and b.
    Paramters
    ---------
    a:
        Describe a
    b:
        describe b
    Returns
    -------
    A 2D array.
    """
    return (((a.x - b.x)**2) + ((a.y - b.y)**2))**0.5

def makeEnvironment():
    """ Read the environment in from a file.
    Returns
    -------
    A 2D array.
    """
    with open('in.txt', newline='') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        environment = []
        for row in reader:
            rowlist = []
            for value in row:
                rowlist.append(value)
            environment.append(rowlist)
    return environment
    
def getTotalEnvironment(environment):
    result = 0
    for row in range(0, len(environment)):
        for col in range(len(environment[row])):
            result += environment[row][col]
    return result

def getTotalAgents(agents):
    result = 0
    for i in range(num_of_agents):
        result += agents[i].store
    return result
    
# Init
random.seed(2)
num_of_agents = 10
num_of_iterations = 5
agents = []
environment = makeEnvironment()

# Make the agents.
agents =[]
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

# Get start totals
startTotalEnvironment = getTotalEnvironment(environment)
print("startTotalEnvironment", startTotalEnvironment)
startTotalAgents = getTotalAgents(agents)
print("startTotalAgents", startTotalAgents)

# Move and eat
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #print(agents[i])
        # Move
        agents[i].move()
        # Eat
        agents[i].eat()

# Get end totals
endTotalEnvironment = getTotalEnvironment(environment)
print("endTotalEnvironment", endTotalEnvironment)
endTotalAgents = getTotalAgents(agents)
print("endTotalAgents", endTotalAgents)

# Test end totals to be sure that nothing got lost
eatenE = startTotalEnvironment - endTotalEnvironment
print(eatenE)
eatenA = endTotalAgents - startTotalAgents 
print(eatenA)
print(eatenA == eatenE)

# Plot
plt.xlim(0, 100)
plt.ylim(0, 100)
# Plot background
plt.imshow(environment)
# Plot agents
for i in range(num_of_agents):
    plt.scatter(agents[i].x, agents[i].y)
plt.show()

# Calculate distances
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
