from eggdrop.egg import Egg
from eggdrop.strategy import EggStrategy
from eggdrop.exceptions import IncorrectResult

class EggDropper(object):
    
    def __init__(self, strategy, building_size, number_of_eggs=2):
        assert isinstance(strategy, EggStrategy), "Please provide a subclass of EggStrategy"
        assert isinstance(building_size, int), "Building size must be an integer"
        assert isinstance(number_of_eggs, int), "Number of eggs must be an integer"
        assert building_size > 0, "Building size must be at least one floor"
        assert number_of_eggs > 0, "You must provide at least one egg"
        
        self.strategy = strategy
        self.building_size = building_size
        self.number_of_eggs = number_of_eggs
        
    def run(self, eggStrength):
        # Provide the strategy with a box of eggs.
        eggbox = [ Egg(eggStrength) for _ in range(0, self.number_of_eggs) ]
        
        copied_eggbox = list(eggbox)
        result = self.strategy.strategize( eggbox, self.building_size)
        
        number_of_drops = sum([egg.get_drop_count() for egg in copied_eggbox])
        number_of_eggs_destroyed = sum([1 for egg in copied_eggbox if egg.is_smashed()])
        
        if not result == eggStrength:
            raise IncorrectResult()
        
        return (number_of_drops, number_of_eggs_destroyed)