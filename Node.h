#ifndef NODE_H
#define NODE_H
#include <iostream>
#include <ostream>

class Node {

  int x;
  int y;
  int id;

  public:
    Node(int, int, int);
    int getx() const;
    int gety() const;
    int getid() const;
    Node& operator= (const Node &node);
    friend std::ostream& operator<<(std::ostream& os, const Node& n);
};

#endif
