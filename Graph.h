#ifndef GRAPH_H
#define GRAPH_H

class Graph {
  std::vector<Node> nodelist;
  //vector<Int> path;
public:
  Graph();
  void add_node(Node x);
};

#endif
