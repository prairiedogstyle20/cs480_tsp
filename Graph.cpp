#include <vector>
#include "Node.h"
#include "Graph.h"

Graph::Graph(){
  std::vector<Node> nodelist{};
}

void Graph::add_node(Node x){
  this -> nodelist.push_back(x);
}

double Graph::getDist(std::vector<Node> list) {
	double value = 0;
	for (int i = 0; i < list.size; i++)
	{
		//Add up all the distances from each node
		//value += list.distance;
	}

	return value;
}

void Graph::Two_Opt() {
	//Get the tour size
	//This is total number of the paths
	int sizeOfTour = nodelist.size;

	// repeat loop until this value reaches some value
	int improvement = 0;

	while (improvement < 25) {
		double lowest_dist = getDist(nodelist);
		for (int i = 0; i < size-1; i++)
		{
			for (int j = i+1; j < size; j++)
			{
				//begin swapping
				Swap(i, k);
				double newDist = getDist(newnodelist);

				if (newDist < lowest_dist) {
					improvement = 0;
					nodelist = newnodelist;
					lowest_dist = newDist;
					//Update Graph Here
				}
			}
		}
		//update improvement iterator
		improvement++;
	}
}

void Swap(const int& i, const int& k) {
	int sizeOfTour = nodelist.size;

}
