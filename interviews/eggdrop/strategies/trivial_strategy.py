import pprint
from eggdrop.strategy import EggStrategy
from eggdrop.eggdropper import EggDropper

class TrivialStrategy(EggStrategy):
    
    NAME = 'Really Dumb Strategy'
    
    def strategize(self, eggbox, building_size):
        myEgg = eggbox.pop()
        
        for floor_no in range(1, building_size + 1):
            result = myEgg.drop(floor_no)
            if result:
                return floor_no - 1
        return building_size
            
if __name__ == "__main__":
    pprint.pprint(EggDropper(TrivialStrategy(), 100).evaluate())