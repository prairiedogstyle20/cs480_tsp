#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "Node.h"
#include "Graph.h"

using namespace std;

bool parse_data_file(Graph);

int main(){
  cout << "TSP PROJECT STARTED";

  Graph *mygraph = new Graph();

  bool generate_data = parse_data_file(*mygraph);

  if (generate_data == true){
    cout << "Data generated successfully" << '\n' << '\n';
  }
  else
    cout << "Data generated failed" << '\n' << '\n';

  return 0;
}

/*
 / simple function to parse csv into data structure
 /
*/
bool parse_data_file(Graph mygraph){
  string currLine;
  int part_counter = 3;
  int curr_x;
  int curr_y;
  int curr_id;

  ifstream myfile("santa_cities.csv");
  if (myfile.is_open())
  {
    while ( getline (myfile,currLine, ',') )
    {
      //cout << part_counter << '\n';
      if(part_counter % 3 == 0){
        curr_id = stoi(currLine);
        //cout << "id = " << curr_id << '\n';
      }
      else if(part_counter % 3 == 1){
        curr_x = stoi(currLine);
        //cout << "x = " << curr_x << '\n';
      }
      else if(part_counter % 3 == 2){
        curr_y = stoi(currLine);
        //cout << "y = " << curr_y << '\n';
      }
      Node *curr_node = new Node(curr_x, curr_y, curr_id);
      cout << *curr_node;
      mygraph.add_node(*curr_node);

      part_counter++;
    }
    myfile.close();
    return true;
  }
  else
    return false;
}
