from itertools import *
def chainslice(start, end, *ranges):
    return islice(chain.from_iterable(ranges), start, end)
