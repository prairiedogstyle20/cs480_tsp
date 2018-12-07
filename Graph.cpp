#include <vector>
#include "Node.h"
#include "Graph.h"

Graph::Graph(){
  std::vector<Node> nodelist{};
}

void Graph::add_node(Node x){
  this -> nodelist.push_back(x);
}
