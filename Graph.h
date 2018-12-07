#ifndef GRAPH_H
#define GRAPH_H
#include <vector>
#include "Node.h"
#include <math.h>

class Graph {
	std::vector<Node> nodelist;
	std::vector<Node> newnodelist;
  double tourTotalLength;
  //vector<Int> path;
public:
  Graph();
  void add_node(Node x);
  double calc_dist(int first_node,int next_node);
  double getDist(std::vector<Node> list);
  void Swap(const int& i, const int& k);
  void Two_Opt();
};

#endif
