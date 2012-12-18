class Egg(object):
    def __init__(self, strength=0):
        self.__strength = strength
        self.__smashed = False
        self.__drop_count = 0
        
    def drop(self, fromFloor):
        self.__drop_count += 1
        
        if self.__smashed:
            raise EggAlreadySmashed()
        
        if fromFloor > self.__strength:
            self.__smashed = True
            return True
            
    def is_smashed(self):
        return self.__smashed 
        
    def get_drop_count(self):
        return self.__drop_count