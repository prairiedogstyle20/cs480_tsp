import math
import csv
import time
import random
import copy
import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getid(self):
        return self.id

class Graph:
    def __init__(self):
        self.nodelist = []
        self.templist = []
        self.path = []
        self.temppath = []
        self.xlist = []
        self.ylist = []
        self.path_cost = 0


    def calc_dist(self,mylist, a, b):
        return math.sqrt((mylist[b].gety() - mylist[a].gety())**2 + (mylist[b].getx()-mylist[a].getx())**2)

    def calc_path_cost(self, pathlist):
        totalCost = 0
        for i in pathlist:
            totalCost = totalCost + i
        return totalCost

    def gen_xlist(self):
        for num in range(len(self.nodelist)-1):
            self.xlist.append(self.nodelist[num].getx())

    def gen_ylist(self):
        for num in range(len(self.nodelist)-1):
            self.ylist.append(self.nodelist[num].gety())

    def twoopt_swap(self):

        #swaps around the lists
        randBegin = random.randint(2,len(self.nodelist)-2)
        randEnd = random.randint(randBegin + 1,len(self.nodelist)-1)
        #print("randBegin = ", randBegin, '\n', "randEnd = ", randEnd)
        self.templist = copy.deepcopy(self.nodelist[0:randBegin])
        reverseList = copy.deepcopy(self.nodelist[randBegin:randEnd])
        endList = copy.deepcopy(self.nodelist[randEnd:])

        #print("Total length = ", len(self.templist)+len(reverseList)+len(endList))

        reverseList.reverse()
        for i in reverseList:
            self.templist.append(copy.deepcopy(i))
        for n in endList:
            self.templist.append(copy.deepcopy(n))

        for i in range(len(self.nodelist)-1):
            if i == len(self.nodelist)-1:
                # this checks for the last value
                # then calculates the distance from the beginning node to the last node
                distance = self.calc_dist(tsp_graph.templist,len(self.nodelist)-1,0)
                self.temppath.append(distance)
            else:
                # this calculates the distance from the current node to the next and appends to path
                distance = self.calc_dist(self.templist,i,i+1)
                self.temppath.append(distance)

        curr_cost = self.calc_path_cost(self.temppath)

        if curr_cost >= self.path_cost:
            self.templist.clear()
            self.temppath.clear()
            improvement = 0
            time_not_updated = 1
            return improvement, time_not_updated

        else:
            time_not_updated = 0
            improvement = (self.path_cost - curr_cost)
            self.nodelist.clear()
            self.nodelist = copy.deepcopy(self.templist)
            self.path.clear()
            self.path = copy.deepcopy(self.temppath)
            self.templist.clear()
            self.temppath.clear()
            self.path_cost = curr_cost
            return improvement, time_not_updated
            #improvement += (self.path_cost - curr_cost)
        #self.templist =



def main():

    # gets the current cpu time
    begin_time = time.process_time()

    #creates a graph object
    tsp_graph = Graph()

    # This loop opens the file and parses each line into a node
    # Then each node is appended to the nodelist in graph object
    with open('santa_cities.csv') as data:
        myreader = csv.reader(data, delimiter=',')
        for row in myreader:
            tsp_graph.nodelist.append(Node(int(row[1]),int(row[2]),int(row[0])))

    for i in range(len(tsp_graph.nodelist)):
        if i == len(tsp_graph.nodelist)-1:
            # this checks for the last value
            # then calculates the distance from teh beginning node to the last node
            distance = tsp_graph.calc_dist(tsp_graph.nodelist,len(tsp_graph.nodelist)-1,0)
            tsp_graph.path.append(distance)
        else:
            # this calculates the distance from the current node to the next and appends to path
            distance = tsp_graph.calc_dist(tsp_graph.nodelist,i,i+1)
            tsp_graph.path.append(distance)

    curr_cost = tsp_graph.calc_path_cost(tsp_graph.path)
    tsp_graph.path_cost = curr_cost
    print("Current Cost = ", curr_cost)

    improvement = 0
    not_updated = 0
    curr_value = 0
    time_not_updated = 0
    iteration = 0
    while time_not_updated != 5:
        curr_value, not_updated = tsp_graph.twoopt_swap()

        if not_updated == 0:
            time_not_updated = 0
        else:
            time_not_updated += 1

        improvement += curr_value
        print("time_not_updated = ",time_not_updated)
        print("iteration = ", iteration)
        iteration += 1

    print("Improvement = ", improvement)

    curr_cost = tsp_graph.calc_path_cost(tsp_graph.path)
    print("Current Cost = ", curr_cost)
    #tsp_graph.gen_xlist()
    #tsp_graph.gen_ylist()
    #plt.rcParams['agg.path.chunksize'] = 20000
    #plt.plot(tsp_graph.xlist,tsp_graph.ylist)

    #plt.show()

    end_time = time.process_time()

    print("Time to calculate path = ", end_time - begin_time, " sec")

main()
