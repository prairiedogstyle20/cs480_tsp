#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool parse_data_file();

int main(){
  cout << "TSP PROJECT STARTED";

  bool generate_data = parse_data_file();
  if (generate_data == true){
    cout << "Data generated successfully" << '\n' << '\n';
  }
  else
    cout << "Data generated failed" << '\n' << '\n';

  return 0;
}

bool parse_data_file(){
  string currLine;
  ifstream myfile("santa_cities.csv");
  if (myfile.is_open())
  {
    while ( getline (myfile,currLine) )
    {
      cout << currLine << '\n';
    }
    myfile.close();
    return true;
  }
  else
    return false;
}
