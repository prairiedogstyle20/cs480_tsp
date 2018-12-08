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
		//get the current distance
		double lowest_dist = getDist(nodelist);

        for (int i = 0; i < sizeOfTour-1; i++)
		{
            for (int j = i+1; j < sizeOfTour; j++)
			{
				//begin swapping
                Graph::Swap(i, j);
				//get the distance of the newlist
				double newDist = getDist(newnodelist);
				//check to see if the new dist is less than the previous record
				if (newDist < lowest_dist) {
					//change current stuff to the better one
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

	//https://en.wikipedia.org/wiki/2-opt
	//The algorithm is based off the psuedo-code on the wiki

    int sizeOfTour = this -> nodelist.size();
	// 1. take route[0] to route[i-1] and add them in order to new_route
	for (int c = 0; c <= i - 1; ++c)
	{
		//HAVE TO IMPLEMENT THIS
		new_tour.SetCity(c, tour.GetCity(c));
	}
    //newnodelist=nodelist;
	// 2. take route[i] to route[k] and add them in reverse order to new_route
	int position = 0;
	for (int c = i; c <= k; ++c)
	{
		new_tour.SetCity(c, tour.GetCity(k - position));
		position++;
	}
    //newnodelist[k]=nodelist[i];
	// 3. take route[k+1] to end and add them in order to new_route
	for (int c = k + 1; c < size; ++c)
	{
		new_tour.SetCity(c, tour.GetCity(c));
	}
	//newnodelist[i] = nodelist[k];
}
