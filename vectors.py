__author__ = 'aaroncraig'

## ----------------------------------------------------------------------
## Imports.
## ----------------------------------------------------------------------

import math


## ----------------------------------------------------------------------
## Vector class.
## ----------------------------------------------------------------------

class Vector(object):

    dimensions = None
    components = None

    def __init__(self, components):
        if not isinstance(components, tuple) and not isinstance(components, list):
            raise ValueError("Components must be a tuple or list.")
        if len(components) == 0:
            raise ValueError("Components must be at least 1-dimensional.")
        self.dimensions = len(components)
        self.components = components

    def __getitem__(self, key):
        return 0 if key >= self.dimensions else self.components[key]

    def __str__(self):
        return self.components.__str__()


## ----------------------------------------------------------------------
## Utility functions.
## ----------------------------------------------------------------------

def dist(v1, v2):
    return math.sqrt(cheap_dist(v1,v2))

def cheap_dist(v1, v2):
    comps1 = v1.components
    comps2 = v2.components
    max_dimensions = max(v1.dimensions, v2.dimensions)
    dist = 0.0
    for i in range(0, max_dimensions):
        dist += math.pow(v1[i]-v2[i] , 2)
    return dist