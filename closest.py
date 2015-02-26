__author__ = 'aaroncraig'

from vectors import dist
from vectors import Vector
from math import floor
import random
from collections import defaultdict
import itertools

def closest_pair(points):

    dimensions = max(map(lambda x: len(x), points))

    s = points[:2]
    delta_x = dist(s[0], s[1])
    pair = [s[0], s[1]]
    grid = Grid(s, delta_x, dimensions)

    for i in range(2, len(points)-1):

        # construct s_i
        s.append(points[i])

        # get points in the neighbourhood of points[i]
        neighbours = [vector for vector in grid.neighbourhood(points[i])]

        # get smallest distance in that neighbourhood
        min = None
        min_pair = None
        for pt in neighbours:
            d = dist(pt, points[i])
            if min == None or d < min:
                min = d
                min_pair = (pt, points[i])

        # was that distance smaller than delta_x?
        if min != None and min < delta_x:
            delta_x = min
            pair = min_pair
            grid = Grid(s, delta_x, dimensions)
        else:
            grid.insert(points[i])

    return pair


class Grid(object):

    grid = None
    mesh_size = None

    def __init__(self, vectors, mesh_size, dimensions):
        self.grid = Mdict(dimensions)
        self.mesh_size = mesh_size
        for v in vectors:
            self.insert(v)

    def _indx(self, vector):
        index = []
        for x in vector:
            index.append( floor(x/self.mesh_size) )
        return index

    def insert(self, vector):
        indx = self._indx(vector)
        self.grid[indx].append(vector)

    def neighbourhood(self, vector):
        centroid = self._indx(vector)
        residuals = []
        for component in centroid:
            residuals.append( [component-1, component, component+1] )
        neighbours = []
        for index in itertools.product(*residuals):
            contents = self.grid[index]
            neighbours += contents
        return neighbours


class Mdict():

    depth = None
    map = None

    def __init__(self, depth):
        tree = lambda x: defaultdict(list) if x == 1 else defaultdict(lambda: tree(x-1))
        self.map = tree(depth)

    def __getitem__(self, vector):
        return self.retrieve(self.map, vector, 0, len(vector)-1)

    def retrieve(self, map, vector, i, stop):
        if i == stop:
            return map[vector[i]]
        else:
            return self.retrieve(map[vector[i]], vector, i+1, stop)

def main():

    pts = [
        Vector([4,3,16]),
        Vector([230,423,150]),
        Vector([123,500,400]),
        Vector([6,4,10]),
        Vector([123,432,432])
    ]
    pair = closest_pair(pts)
    print(pair[0])
    print(pair[1])

if __name__ == "__main__": main()