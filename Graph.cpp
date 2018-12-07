#include "Graph.h"

Graph::Graph(){
  std::vector<Node> nodelist{};
}

void Graph::add_node(Node x){
  this -> nodelist.push_back(x);
}

double Graph::calc_dist(int first_node,int next_node)
{
    double xdiff;
    double ydiff;
    xdiff= pow(nodelist[next_node].getx()-nodelist[first_node].getx(),2);
    ydiff= pow(nodelist[next_node].gety()-nodelist[first_node].gety(),2);
    return sqrt(abs(xdiff+ydiff));

}

double Graph::getDist(std::vector<Node> list) {
	double value = 0;
    for (int i = 0; i < list.size(); i++)
	{
		//Add up all the distances from each node
        if (i!=(list.size()-1))
        {
            value += Graph::calc_dist(i,i+1);
        }
	}

	return value;
}

void Graph::Two_Opt() {
	//Get the tour size
	//This is total number of the paths
    int sizeOfTour = nodelist.size();

	// repeat loop until this value reaches some value
	int improvement = 0;

	while (improvement < 25) {
		double lowest_dist = getDist(nodelist);
        for (int i = 0; i < sizeOfTour-1; i++)
		{
            for (int j = i+1; j < sizeOfTour; j++)
			{
				//begin swapping
                Graph::Swap(i, j);
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

void Graph::Swap(const int& i, const int& k) {
    int sizeOfTour = this -> nodelist.size();
	// 1. take route[0] to route[i-1] and add them in order to new_route
    newnodelist=nodelist;
	// 2. take route[i] to route[k] and add them in reverse order to new_route
    newnodelist[k]=nodelist[i];

    newnodelist[i]=nodelist[k];
	// 3. take route[k+1] to end and add them in order to new_route
}
