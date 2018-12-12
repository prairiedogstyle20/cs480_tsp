import math
import csv
import time
import random
import copy
import pprint
import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        self.dist = 0

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getid(self):
        return self.id

    def getdist(self):
        return self.dist

    def set_dist(self,newdist):
        self.dist = newdist

################################################################################
################### end of class ###############################################
################################################################################

class Graph:
    def __init__(self):
        self.nodelist = []
        self.templist = []
        self.path = []
        self.temppath = []
        self.xlist = []
        self.ylist = []
        self.path_cost = 0
        self.kvalue = 2

    def getk(self):
        return self.kvalue

    def calc_dist(self,a, b):
        return math.sqrt((b.gety() - a.gety())**2 + (b.getx()-a.getx())**2)

    def calc_path_cost(self, pathlist):
        totalCost = 0
        for i in pathlist:
            totalCost = totalCost + i.getdist()
        return totalCost

    def gen_xlist(self):
        for num in range(len(self.nodelist)-1):
            self.xlist.append(self.nodelist[num].getx())

    def gen_ylist(self):
        for num in range(len(self.nodelist)-1):
            self.ylist.append(self.nodelist[num].gety())

    def build_kdtree(self, points, depth=0):
        n = len(points)
        #with open("output.txt", "a") as myfile:
        #    myfile.write(f"Depth = {depth}, list length = {n}")

        if n <=0:
            return None

        axis = depth % self.getk()

        if axis == 0:
            sorted_points = sorted(points, key=lambda point:point.x)
        else:
            sorted_points = sorted(points, key=lambda point:point.y)

        return{ 'point': sorted_points[int(n/2)],
                'left': self.build_kdtree(sorted_points[:int(n/2)], depth +1),
                'right': self.build_kdtree(sorted_points[int(n/2) + 1:], depth +1)
              }

    def NNS_KDtree(self,root, search_point, path_list, depth=0, currBest=None):
        if root is None:
            return currBest

        axis = depth % self.getk()

        new_currBest = None
        next_branch = None

        if currBest is None:
            new_currBest = root['point']

        elif self.calc_dist(search_point, currBest) > self.calc_dist(search_point, root['point']) and root['point'] not in path_list:
            #print('Search point id = ', search_point.getid())
            #print('curr best = ',self.calc_dist(search_point, root['point']))
            #print('id = ',root['point'].getid())
            new_currBest = root['point']
        else:
            new_currBest = currBest

        if axis == 0:
            if search_point.getx() < root['point'].getx():
                next_branch = root['left']
            else:
                next_branch = root['right']
        else:
            if search_point.gety() < root['point'].gety():
                next_branch = root['left']
            else:
                next_branch = root['right']
        return self.NNS_KDtree(next_branch, search_point,  path_list, depth +1, new_currBest)



################################################################################
################### end of class ###############################################
################################################################################


def main():

    pp = pprint.PrettyPrinter(indent=4)

    begin_time = time.process_time()
    tsp_graph = Graph()

    # This loop opens the file and parses each line into a node
    # Then each node is appended to the nodelist in graph object
    with open('santa_cities.csv') as data:
        myreader = csv.reader(data, delimiter=',')
        for row in myreader:
            tsp_graph.nodelist.append(Node(int(row[1]),int(row[2]),int(row[0])))

    #tsp_graph.templist = copy.deepcopy(tsp_graph.nodelist)
    mytree = tsp_graph.build_kdtree(tsp_graph.nodelist)
    #add first node to path
    tsp_graph.path.append(tsp_graph.nodelist[0])

    #loop through and append the nearest neighbor to graph path cost
    index = 0
    while index < len(tsp_graph.nodelist) - 1:
        #print(index)
        tsp_graph.path.append(tsp_graph.NNS_KDtree(mytree, tsp_graph.path[index], tsp_graph.path))

        index += 1

    cost = 0

    with open('ouput.txt','w') as file:
        for num in range(len(tsp_graph.path) - 1):
            file.write(str(tsp_graph.path[num].getid()))
            file.write('\n') 
    print(tsp_graph.path[0].getid())
    #for num in range(len(tsp_graph.path) - 1):
        #print(tsp_graph.path[num].getid())
        #cost += tsp_graph.calc_dist(tsp_graph.path[num], tsp_graph.path[num + 1])
    #print('Path Cost = ', cost)
    #print(NN.getid(), tsp_graph.nodelist[5000].getid())
    end_time = time.process_time()
    print("Time to calculate path = ", end_time - begin_time, " sec")

#executes the program
main()
