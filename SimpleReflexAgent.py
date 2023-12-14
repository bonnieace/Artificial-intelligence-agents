import random
class Environment():
    def __init__(self):
        self.Location=random.randint(1,2)
        self.LocationCondition=random.randint(0,1)
    
    def displayLocation (self):
        print("The Agent is in position :"+str(self.Location))

    def displayLocationCondition (self):
        if self.LocationCondition==0:
            print("The Location is clean")
        else:
            print("The Location is dirty")
        
    
class Agent(Environment):
    def __init__(self,environment):
        environment.displayLocation()
        environment.displayLocationCondition()

       
        if environment.LocationCondition==1:
            environment.LocationCondition==0
            print("Location " + str(environment.Location) + " has been cleaned")
            

Env=Environment()
Ag=Agent(Env)
                





     
