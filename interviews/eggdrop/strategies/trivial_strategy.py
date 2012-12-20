from eggdrop.strategy import EggStrategy
from eggdrop.eggdropper import EggDropper

class TrivialStrategy(EggStrategy):
    def strategize(self, eggbox, building_size):
        myEgg = eggbox.pop()
        
        for floor_no in range(1, building_size + 1):
            result = myEgg.drop()
            if result:
                return floor_no - 1
            
if __name__ == "__main__":
    EggDropper.run(TrivialStrategy(), 100)