from eggdrop.strategy import EggStrategy


def get_interval(building_size):
    """Brute-force optimization for the average number of drops required in
    when the egg strength is random.
    """
    interval = float("infinity")
    for i in xrange(1, building_size+1):
        interval = min(interval, round(building_size/2/i) + i)
    return int(interval)


class IntervalStrategy(EggStrategy):
    """This strategy splits the size of the building up into a number
    of equal sized intervals.  It then finds the first interval where the
    first entry results in an egg breaking and then does a linear search on
    the preceding interval.

    This has better average and worst-case if the eggbox has two eggs and the
    building size is 100 but this is not necessarily the case if these
    parameters are varied.

    A good strategy would calculate performance characteristics depending on
    parameters and select the best algorithm accordingly (e.g. binary chop for
    high buildings with a low number of eggs).  It would switch algorithms at
    runtime as the number of levels that need to be check and the number of
    available eggs decrease.
    """

    NAME = "Interval Strategy"

    def strategize(self, eggbox, building_size):
        it = iter(eggbox)
        egg = it.next()
        interval = get_interval(building_size)
        for level in xrange(1, building_size+1, interval):
            if not egg.drop(level):
                continue
            egg = it.next()
            for level in xrange(level-interval+1, level+1):
                if egg.drop(level):
                    return level - 1

        # Check the last interval.
        for level in xrange(level-interval+1, building_size+1):
            if egg.drop(level):
                return level - 1

        return building_size


if __name__ == '__main__':
    import pprint
    from eggdrop.eggdropper import EggDropper

    pprint.pprint(EggDropper(IntervalStrategy(), 100).evaluate())
