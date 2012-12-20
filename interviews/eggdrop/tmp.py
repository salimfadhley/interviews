"""
Here is one that is actually an optimization problem:

The problem is simple: You have to figure out from which floor an egg can fall from a 100 story building before it breaks. 
Given data:
a.    You have got 2 eggs. These might break from the first floor or might even survive a drop from the 100th floor. Yes these are some special kind of eggs which break on floor number X and X needs to be determined.
b.    If you drop an egg and it doesn't break, you can assume that the impact of fall has no effect on its strength. The egg is as strong as new one.
c.    You are allowed to break both eggs as long as you can determine the floor from with both of them will break (out of 100) 
Question is to find out the most efficient way to drop the eggs and determine the answer i.e. the algorithm to drop the eggs which minimizes the number of egg drops.

The lamest way to do it is take one egg and keep dropping it from every floor till it breaks. That will take a max of 99 tries. 

If you feel more adventurous you can generalize your solution for n floors and e eggs. 
"""

class EggAlreadySmashed(Exception): pass


      
class RubbishStrategy(EggStrategy):
    NAME = "Rubbish"
    
    def strategize(self, eggbox, building_size):
        while eggbox:
            eggbox.pop()
        return 0

class RubbishStrategy2(EggStrategy):
    NAME = "Rubbish2"
    
    def strategize(self, eggbox, building_size):
        for egg in eggbox:
            egg.drop(building_size+1)
        return 0


    
