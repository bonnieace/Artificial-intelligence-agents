import random
import time
class Environment:
    def __init__(self):
        self.LocationCondition=random.randint(0,1)
        self.cleaningMode=random.choice(["T","L"])
        

class Agent(Environment):
    def __init__(self,environment):
        print("Previous History:"+environment.cleaningMode)
        
        if environment.LocationCondition==1:
            if environment.cleaningMode=="T":

                environment.cleaningMode="L"


            else:
                environment.cleaningMode="T"

            
            print("Location  is dirty")

            environment.LocationCondition=0
            print("Location  has been  cleaned ")
            print("updated history",environment.cleaningMode)


        
        else:
            print("Location  is clean")

        print("________________________")

            

        
       




        
x=0

while x<24:
    Env=Environment()

    Ag=Agent(Env)
    x+=1
    time.sleep(1)


            




                    