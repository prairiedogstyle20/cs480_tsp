#include "Node.h"

Node::Node(int x, int y, int id){
  this->x = x;
  this->y = y;
  this->id = id;
}

int Node::getx() const{
  return x;
}

int Node::gety() const{
  return y;
}

int Node::getid() const{
  return id;
}

Node& Node::operator= (const Node &node)
{
    this->x = node.getx();
    this->y = node.gety();
    this->id = node.getid();
    return *this;
}


std::ostream & operator<<(std::ostream& os, const Node& n){
  os << "ID = " << n.getid() << '\n'
     << "X = " << n.getx() << '\n'
     << "Y = " << n.gety() << "\n\n";
}
