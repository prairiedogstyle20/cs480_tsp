#ifndef GRAPH_H
#define GRAPH_H

class Graph {
	std::vector<Node> nodelist;
	std::vector<Node> newnodelist;
  double tourTotalLength;
  //vector<Int> path;
public:
  Graph();
  void add_node(Node x);
  void getDist(std::vector<Node> list);
  void Swap(const int& i, const int& k);
  void Two_Opt();
};

#endif
