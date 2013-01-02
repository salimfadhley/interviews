#!/usr/bin/env python

import unittest

from eggdrop.egg import Egg
from eggdrop.strategies.interval_strategy import IntervalStrategy

def  with_params(egg_strength, building_size=100, num_eggs=2):
    def decorator(fn):
        def wrapper(self):
            eggs = [Egg(egg_strength) for _ in xrange(num_eggs)]
            return fn(self, eggs, building_size)
        return wrapper
    return decorator


class TestIntervalStrategy(unittest.TestCase):

    def setUp(self):
        super(TestIntervalStrategy, self).setUp()
        self.strat = IntervalStrategy()

    @with_params(egg_strength=1)
    def test_eggstrength_1(self, eggs, building_size):
        self.assertEqual(self.strat.strategize(eggs, building_size), 1)

    @with_params(egg_strength=50)
    def test_eggstrength_50(self, eggs, building_size):
        self.assertEqual(self.strat.strategize(eggs, building_size), 50)

    @with_params(egg_strength=99)
    def test_eggstrength_99(self, eggs, building_size):
        self.assertEqual(self.strat.strategize(eggs, building_size), 99)

    @with_params(egg_strength=100)
    def test_eggstrength_100(self, eggs, building_size):
        self.assertEqual(self.strat.strategize(eggs, building_size), 100)

    @with_params(egg_strength=101)
    def test_eggstrength_101(self, eggs, building_size):
        self.assertEqual(self.strat.strategize(eggs, building_size), 100)


if __name__ == '__main__':
    unittest.main()
