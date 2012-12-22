from unittest import TestCase

from eggdrop.egg import Egg
from eggdrop.eggdropper import EggDropper
from eggdrop.strategy import EggStrategy

class TestEggDrop(TestCase):
    
    def testLuckyGuessDumbStrategy(self):
        
        class DumbStrategy(EggStrategy):
            NAME = "Sal's Dumb strategy"
            def strategize(self, eggbox, building_height):
                while eggbox:
                    egg = eggbox.pop()
                    for building_level in range(0, building_height):
                        if egg.drop(building_level):
                            return building_level - 1
        
        dropper = EggDropper( DumbStrategy(), 100, 1 )
        print = dropper.run(50)

                        