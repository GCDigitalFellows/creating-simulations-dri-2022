import random
import statistics as stats

# create new die class that specifies how many sides
class Die:  
    def __init__(self, sides):  
        self.sides = sides 
    
    # create a 'roll' method to return a random # between 1-6
    def roll(self):
        return random.randint(1, self.sides)

# create new die object, roll the die, and print the results
die = Die(6)   
print(die.roll()) 


class DiceSim:
    """Rolls our dice x amount of times and prints the results

    Arguments:
        dice_method: The dice method that we'll pass in
        iterations: The number of times to run the sim"""

    def __init__(self, dice_method, iterations):
        # take initial parameters
        self.dice_method = dice_method
        self.iterations = iterations
        # create a new empty list and run method call
        self.results = []
        self.run()

    # run our die roll method and store the results
    def run(self):
        for i in range(self.iterations):
            result = self.dice_method()
            self.results.append(result)
        self.report()

    # report the results of the analysis
    def report(self):
        max_num = max(self.results) 
        min_num = min(self.results) 
        mean = stats.mean(self.results) 
        median = stats.median(self.results)
        #print results with a multi-line f-string
        print( 
            f"""Number of Simulations: {self.iterations}
            Max: {max_num}
            Min: {min_num}
            Mean: {mean}
            Median: {median}"""
        )

# create new class objects and run the simulator, passing in our die object and method
die1 = Die(6)
sim = DiceSim(die1.roll, 1000)

