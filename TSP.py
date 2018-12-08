import math
import csv
import time

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
        self.path = []

    def calc_dist(self, a, b):
        return math.sqrt((self.nodelist[b].gety() - self.nodelist[a].gety())**2 + (self.nodelist[b].getx()-self.nodelist[a].getx())**2)

    def calc_path_cost(self):
        totalCost = 0
        for i in self.path:
            totalCost = totalCost + i
        return totalCost

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
            distance = tsp_graph.calc_dist(len(tsp_graph.nodelist)-1,0)
            tsp_graph.path.append(distance)
        else:
            # this calculates the distance from the current node to the next and appends to path
            distance = tsp_graph.calc_dist(i,i+1)
            tsp_graph.path.append(distance)

    curr_cost = tsp_graph.calc_path_cost()
    print("Current Cost = ", curr_cost)

    end_time = time.process_time()

    print("Time to calculate path = ", end_time - begin_time, " sec")

main()
