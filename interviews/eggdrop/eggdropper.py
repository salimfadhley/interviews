import pprint
import random
import logging
import collections
from eggdrop.egg import Egg
from eggdrop.strategy import EggStrategy
from eggdrop.exceptions import IncorrectResult

log = logging.getLogger(__name__)

DropperResult = collections.namedtuple('DropperResult', ("got_correct_answer", "number_of_drops", "number_destroyed"))
DropperEvaluation = collections.namedtuple('DropperEvaluation', ('strategy_name','avg_correct', 'avg_drops', 'avg_destroyed', 'worst_case_scenario'))

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
        
    
    def evaluate(self):
        results = []
        
        all_floors = list(range(1, self.building_size + 1))
        random.shuffle(all_floors)
        
        for floor_no in all_floors:
            results.append(self.run(floor_no)) 
            
        avg_correct = sum( r.got_correct_answer for r in results ) / len(results)
        avg_drops = sum( r.number_of_drops for r in results ) / len(results)
        avg_destroyed = sum( r.number_destroyed for r in results ) / len(results)
        worst_case_scenario = max( r.number_of_drops for r in results )
        
        evaluation = DropperEvaluation(self.strategy.NAME,avg_correct,avg_drops,avg_destroyed,worst_case_scenario)
        return evaluation
        
    def run(self, eggStrength=None):
        log.debug("Checking %s with %i eggs of strength %i" % (self.strategy.NAME, self.number_of_eggs, eggStrength))
        if not eggStrength:
            eggStrength = random.randint(1, self.building_size + 1)
        
        # Provide the strategy with a box of eggs.
        eggbox = [ Egg(eggStrength) for _ in range(0, self.number_of_eggs) ]
        
        copied_eggbox = list(eggbox)
        result = self.strategy.execute_strategy( eggbox, self.building_size)
        
        got_correct_answer = result == eggStrength
        number_of_drops = sum([egg.get_drop_count() for egg in copied_eggbox])
        number_of_eggs_destroyed = sum([1 for egg in copied_eggbox if egg.is_smashed()])
        
        if not got_correct_answer:
            log.error("Wrong answer %r" % result)
        
        return DropperResult(got_correct_answer, number_of_drops, number_of_eggs_destroyed)
    