import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import csv

num_of_agents = 10
num_of_iterations = 100
agents = []

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

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

environment = makeEnvironment()


#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

def update(frame_number):
    
    fig.clear()   

    # Plot
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    # Plot background
    matplotlib.pyplot.imshow(environment)

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

matplotlib.pyplot.show()

