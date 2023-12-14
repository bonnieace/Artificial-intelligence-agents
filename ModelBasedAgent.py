import random
class Environment():
    def __init__(self):
        self.Location=random.randint(1,2)
        self.LocationCondition=random.randint(0,1)
        self.cleaningmode=random.choice(["T","L"])

    def DisplayEnvironment(self):
        print("The Vaccum is in Location "+str(self.Location))
        if self.LocationCondition==0:
            print("Location "+str(self.Location)+" is clean")
        else:
            print("Location "+str(self.Location)+" is dirty")
        
        if self.cleaningmode=="T":
            print("Location "+str(self.Location)+" was thoroughly cleaned before")
        else:
            print("Location "+str(self.Location)+" was Lightly cleaned before")

class Agent(Environment):
    def __init__(self,environment):
        environment.DisplayEnvironment()

        if environment.LocationCondition==1:
            if environment.cleaningmode=="T":
                environment.cleaningmode="L"
                print("Location "+str(environment.Location)+" has been cleaned lightly")
            else:
                 environment.cleaningmode="T"
                 print("Location "+str(environment.Location)+" has been cleaned Thoroughly")

Env=Environment()
Ag=Agent(Env)
                





 



