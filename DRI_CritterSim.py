import random

# create global variables
startPopulation = 50  
year = 0  
resources = 2   
food = 0    
fertility_x = 10  
fertility_y = 20             
critterList = []  

disasterChance = 10   

# create Critter class
class Critter:
    def __init__(self, age):
        self.sex = random.randint(0,1)  
        self.age = age 
    
    # critter gather food method
    def gather(food, resources):
        # check if we have able critters
        ableCritters = 0
        for critter in critterList:
            if critter.age > 10 and critter.age < 40:
                ableCritters += 1
        food += ableCritters * resources
        print(f"Food stockpile: {food}.")
        print(f"Able critters: {ableCritters}.")
        
        # delete critters based on starvation level
        if food < len(critterList):
            del critterList[0:int(len(critterList) - food)] 
            food = 0
            print(f"Some critters starved to death! :(")
        else:
            food -= len(critterList) 

        # print results 
        print(f"Population after starvation/feeding is: {len(critterList)}.")
        print(f"After eating, food stockpile is currently {food}.") 

    # critter reproduction method
    def reproduce(fertility_x, fertility_y):
        initial_pop = len(critterList)    
        
        for critter in critterList:
            if critter.sex == 1:    
                if critter.age >= fertility_x: 
                    if critter.age <= fertility_y:
                        if random.randint(0, 4) == 1:  
                            critterList.append(Critter(0)) 
                            
        if initial_pop < len(critterList):    
            print("New critters were born!")
        else:
            print("No new critters were born this year.")                  

# populate the simulator with critter objects
def popSim():
    for x in range(startPopulation):
        critterList.append(Critter(random.randint(2,45)))           

# run each year of the simulation
def runYear(food, resources, fertility_x, fertility_y):
    # run methods
    Critter.gather(food, resources)
    Critter.reproduce(fertility_x, fertility_y)
    
    # age critters
    for critter in critterList:
        if critter.age > 50:
            critterList.remove(critter) 
        else:
            critter.age +=1
    
    # calculate disaster chance
    if random.randint(0, 100) < disasterChance:  
            del critterList[0:int(random.uniform(0.05,0.2)*len(critterList))]  
            print("A disaster has occurred!")
            print(f"There are now {len(critterList)} surviving critters.")

    print(f"After reproducing and/or any disasters, critter population is currently {len(critterList)}.")

# populate simulator
print("--------The Critter Simulation has begun!---------\n\n")
popSim()

# run simulation until population limit is reached
while len(critterList) < 100 and len(critterList) > 1:
    runYear(food, resources, fertility_x, fertility_y)
    year += 1
    print(f"Current year: {year}\n")