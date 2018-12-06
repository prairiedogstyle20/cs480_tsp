#include "Node.h"

Node::Node(int x, int y, int id){
  this->x = x;
  this->y = y;
  this->id = id;
}

int Node::getx(){
  return x;
}

int Node::gety(){
  return y;
}

int Node::getid(){
  return id;
}
