import pprint
from eggdrop.strategy import EggStrategy
from eggdrop.eggdropper import EggDropper

class SlightlyBetterStrategy(EggStrategy):
    
    NAME = 'Slightly Better Strategy'
    
    def strategize(self, eggbox, building_size):
        """
        Binary chop until you get to your last egg,
        and then count up
        """
        lower_bound = 1
        upper_bound = building_size + 1
        
        for egg in eggbox:
            while not egg.is_smashed():
                if upper_bound == lower_bound:
                    return upper_bound
                    
                if self.numIntactEggs() > 1 and ((upper_bound-lower_bound) > 4):
                    mid_point = int((upper_bound-lower_bound)/2) + lower_bound
                    
                    if egg.drop(mid_point):
                        # Egg has smashed
                        upper_bound = mid_point - 1
                        continue
                    else:
                        # Egg did not break
                        lower_bound = mid_point    
                else:
                    if egg.drop(lower_bound + 1):
                        return lower_bound
                    else:
                        lower_bound += 1
            
if __name__ == "__main__":
    pprint.pprint(EggDropper(SlightlyBetterStrategy(), 100).evaluate())