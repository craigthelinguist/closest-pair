__author__ = 'aaroncraig'

from vectors import dist
from vectors import Vector
from math import floor
import random
from collections import defaultdict

def closest_pair(points):

    s = points[:2]
    delta_x = dist(s[0], s[1])
    pair = [s[0], s[1]]
    grid = Grid(s, delta_x)

    for i in range(2, len(points)-1):

        # construct s_i
        s.append(points[i])

        # get points in the neighbourhood of points[i]
        neighbours = []
        neighbourhood = grid.neighbourhood(points[i])
        for box in neighbourhood:
            neighbours += grid.report(box[0], box[1])

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
            grid = Grid(s, delta_x)
        else:
            grid.insert(points[i])

    return pair


class Grid(object):

    grid = None
    mesh_size = None

    def __init__(self, points, mesh_size):
        self.grid = defaultdict(lambda: defaultdict(list))
        self.mesh_size = mesh_size
        for pt in points:
            indx_x = floor(pt[0] / mesh_size)
            indx_y = floor(pt[1] / mesh_size)
            self.grid[indx_x][indx_y].append(pt)

    def insert(self, point):
        indx_x = floor(point[0] / self.mesh_size)
        indx_y = floor(point[1] / self.mesh_size)
        self.grid[indx_x][indx_y].append(point)


    def report(self, indx_x, indx_y):
        return self.grid[indx_x][indx_y]

    def neighbourhood(self, point):
        x = floor(point[0] / self.mesh_size)
        y = floor(point[1] / self.mesh_size)
        return [(x-1,y-1), (x,y-1), (x,y+1),
                (x-1,y), (x,y), (x+1,y),
                (x-1,y+1), (x,y+1), (x+1,y+1)]



def main():
    pts = [Vector([4,2]), Vector([15,23]), Vector([14,60]), Vector([5,10]), Vector([6,14])]
    pair = closest_pair(pts)
    print(pair[0])
    print(pair[1])
    print(pair)

if __name__ == "__main__": main()