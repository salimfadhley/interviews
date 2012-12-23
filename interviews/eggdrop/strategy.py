class EggStrategy(object):
    
    NAME = "Unnamed Strategy"
    
    def execute_strategy(self, eggbox, building_size):
        self.__eggbox = eggbox
        return self.strategize(eggbox, building_size)
    
    def numIntactEggs(self):
        return sum( [1 for e in self.__eggbox if not e.is_smashed()] )
    
    def strategize(self, eggbox, building_size):
        return 0
        
    def __repr__(self):
        return "<%s.%s %s>" % (self.__class__.__module__, self.__class__.__name__, str(self))
        
    def __str___(self):
        return self.NAME