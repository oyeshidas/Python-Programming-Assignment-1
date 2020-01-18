import random

class Agent:
    
    def __init__(self, environment,agents):
        self.environment = environment
        self.agents = agents
        self.store = random.randint(0, 99)
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        
    def __str__(self):
        return "x " + str(self.x) + ", y" + str(self.y) + ", store " + str(self.store)
    
    def move(self):
        if (random.random() < 0.5):
            self.x += 1
        else :
            self.x -= 1
        if (random.random() < 0.5):
            self.y += 1
        else :
            self.y -= 1
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def shareshare_with_neighbours(self,neighbourhood):
        #find out who is near me
        for i in range(0, len(self.agents)):
            distance = self.distance(self.agents[i])
            if (distance <= neighbourhood):
                print("distance",distance)
                #share resources
                total = self.store + self.agents[i].store
                print("total", total)
                ave = total/2
                self.store = ave 
                self.agents[i].nottoshare = ave
                
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5           
          
                