import logging
from eggdrop.exceptions import AttemptedToDropADesroyedEgg

log = logging.getLogger(__name__)

class Egg(object):
    def __init__(self, strength=1):
        assert strength > 0, "The minimum strength of an egg is 1"
        
        self.__strength = strength
        
        self.__smashed = False
        self.__drop_count = 0
        
    def drop(self, fromFloor):
        """
        Return True if dropping an egg results in it's destruction,
        otherwise return False.
        
        Once destroyed an egg cannot be reused!
        """
        self.__drop_count += 1
        
        if self.__smashed:
            # You cannot drop an egg which has already been smashed!
            raise AttemptedToDropADesroyedEgg()
        
        if fromFloor > self.__strength:
            self.__smashed = True
            log.info("I dropped an egg from floor %i and it smashed into little pieces!" % fromFloor)
            return True
        
        log.info("I dropped an egg from floor %i but it did not break" % fromFloor)
        return False
            
    def is_smashed(self):
        return self.__smashed 
        
    def get_drop_count(self):
        return self.__drop_count