import math
import csv

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
        if self.nodelist[b].getx()-self.nodelist[a].getx() == 0:
            return abs((self.nodelist[b].gety() - self.nodelist[a].gety()))
        else:
            return abs((self.nodelist[b].gety() - self.nodelist[a].gety())/(self.nodelist[b].getx()-self.nodelist[a].getx()))
    def calc_path_cost(self):
        totalCost = 0
        for i in self.path:
            totalCost = totalCost + i
        return totalCost

def main():
    tsp_graph = Graph()

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

main()
