class EggStrategy(object):
    
    NAME = "Unnamed Strategy"
    
    def strategize(self, eggbox, building_size):
        return 0
        
    def __repr__(self):
        return "<%s.%s %s>" % (self.__class__.__module__, self.__class__.__name__, str(self))
        
    def __str___(self):
        return self.NAME