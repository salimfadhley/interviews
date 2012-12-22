import unittest
from eggdrop.exceptions import AttemptedToDropADesroyedEgg
from eggdrop.egg import Egg

class TestEgg(unittest.TestCase):
    
    def test_make_egg(self):
        myEgg = Egg(6)
        assert not myEgg.drop(5)
        assert not myEgg.drop(6)
        assert myEgg.drop(7)
        
        with self.assertRaises(AttemptedToDropADesroyedEgg):
            myEgg.drop(0)