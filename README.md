# HW4-ADM-GROUP26
Network analysis

The scripts proposed in this repository solve the exercises in Homework 4, Algorithmic Methods for Data Mining, Master's degree in Data Science, Sapienza University of Rome. 

## Data

The data in usage is the DBLP data set. It contains information concerning Computer Science academic publications, in json format.  
In particular, not only the complete but also a reduced version of the data set are taken into account. 
The user is allowed to choose the data to be analysed. 

## Procedures 
> * Exercise 1:
First of all, through the function 'choose data' the user is allowed to choose whether to load full or reduced json file. 
Then the function ‘import data’ import the file chosen by the user.
By the ‘create graph’ this rawdata is elaborated and a graph like structure is obtained from it, having as weight of  edges the Jaccard distance between the nodes. In order to obtain the graph, the following procedure is used. It is necessary to iterate through all the authors of the entire collection of publications. In case a new author is found, a vertex is created and its attributes are initialized. At each iteration, moreover, the attributes are updated. Once, the vertices have been defined, it is possible to connect them by edges as previously explained. The strategy adopted involves defining a nested list in which every inner array contains the author ids associated with a given publication. Each distinct combination of researchers in any inner list is connected by an edge, properly weighted.
Using the library function of networkx, we retrieve information on the graph. (nx.info())

> * Exercise 2:
After a conference id is taken as input from the user, a list of authors who participated to the conference is built and used to create a subgraph (using subgraph method from networkx library).
Then, by calling the ‘compute centrality measures’ function on the obtained subgraph we assign to dict_dc, dict_close, dict_bet, dict_eig respectively the values of degree, closeness, betweenness and eigenvector centrality. Through ’centrality measures plot’, for each centrality measure, strip plot and bar chart are plotted. Acting  on these centrality dictionaries, ‘scatter plot matrix’ function shows the pairwise relationships between these centrality measures. And the ‘draw violins’ function gives the violin plots if there are at least 15 different values for a given measure.
Calling the ‘bar plot degree’ on the subgraph we obtain a bar plot having in x-axis the degrees and in y-axis their respective frequencies.
For the  second part of the exercise, the user is asked to give an author id and an integer as input, and from those, by calling the ‘hop d’ function a set containing all the author ids up to distance d from the author id given in input is returned. With this set, calling again the networkx library function subgraph, a subgraph containing these author ids as nodes is built and then shown by the ‘plot graph’ function. The developed algorithm is a recursive one. At the first level of the recursion tree, the neighbours of the input node are stored in a set. The procedure continues by adding, at each level, the distinct neighbours of the nodes included at the previous step. Each time the function is called, d is decreased until the base case is reached, i.e. d=0.

> * Exercise 3:
In this part, the user is asked for a target node to calculate the shortest distance from it to Aris. Here, in order to calculate it, the usage of the ‘shortestPath’ function implementing a Dijkstra algorithm is needed.
This function prints out the shortest path weight if the nodes are connected, if not, it prints a message saying whether the target node is actually a part of the graph or the nodes are not connected between each-other.
Finally, for the last task, with the help of ‘shortestPath all’ function, after the user puts in input a query composed of author ids, this function returns a dictionary where the keys are the nodes of the graph and the values are the weights of the minimum shortest distance between the node and one of the query items.
Afterwards, a nice printout of the result obtained Is shown.
The developed algorithm is a recursive one. At the first level of the recursion tree, the neighbours of the input node are stored in a set. The procedure continues by adding, at each level, the distinct neighbours of the nodes included at the previous step. Each time the function is called, d is decreased until the base case is reached, i.e. d=0.


## Script descriptions

1. __`main.py`__:
> This module calls the functions contained in the scripts below in orded to tidily present the results of the exercises given in 
[Homework 4](http://aris.me/contents/teaching/data-mining-ds-2017/homeworks/homework4.pdf). The user may be prompted for input.

2. __`graph.py`__:
> This module provides the code necessary in order to load the chosen data set and creates a graph to model them. 
> The packages required: json, networkx,  combinations (from itertools), matplotlib.pyplot.
>	Four functions are provided:

>  * choose_data(): *the user is prompted to choose the complete or reduced data set.*
>  * import_data(full): *returns the desired data set based on the user's choice (full is a boolean variable, set True if the user's
choice in the function 'choose_data' was y).*
>  * create_graph(data_to_load): *from the required data set as input, returns the relative graph.*
>  * plot_graph(G, color, author = None): *takes as input the graph G, the color which the user want the graph is displayed and if
asked, the author whose the user want to see the node in the graph. Returns the graph plotted of the color asked ( with a different color for the autor in input, if specified).*

3.__`centrality.py`__:
> This script contains functions that allows to compute and visualize different centrality measures associated with each node in the 
> graph.
> The packages required: seaborn, pandas, matplotlib.pyplot, networkx, collections.
> The following procedures are defined:

> * compute_centrality_measures(subgr): *takes as input a subgraph built on the authors who published at least once in the asked 
conference. Returns four measures for each node: degree, betweeness, closeness and eigenvector centrality. The measures are collected in dictionaries, one for each measure, where the key is the node and the value is the measure for that node.*
> * bar_plot_degree(G): *given the graph G as input, it displays a bar chart of the node degrees.*
> * bar_plot(d): *d is one of the measures computed in the function 'compute_centrality_measure' (type : dictionary).
The result is a bar chart useful in order to visually assess every centrality measure is obtained.*
> * strip_plot(d): *as the function 'bar_plot' takes in input one of the measures (d) and a strip-plot is built as an alternative to the bar-chart.* 
> * centrality_measures_plot(dict_dc, dict_close, dict_bet, dict_eig): *the input are all the measures calculated before, the code of this function displays a plot including a bar chart and a strip-plot for each centrality measure.*
> * scatterplot_matrix(dict_dc, dict_bet, dict_close, dict_eig): *from the measures as input a scatterplot matrix is built. This is useful when the aim is exploring the relationship between the different centrality measures. On the main diagonal, histograms are displayed, which is appropriate only when the number of distinct values of the measures is not extremely low.*
> * violin_plot(x, title): *shows the violin plot of x, allows to specify the title.*
> * draw_violins(lst_dict): *the input is a list of the measures for each nodes. The output is a violin plot if the values in a dictionary are at least 15.*

4.__`hop_distance.py`__:
> The package required: networkx. 
> This file is composed by a single function:

> * hop_d(children, dist, output_set, G): *this is a recursive function that, given author (children), an integer (d), an empty set (output_set) and the graph G, returns the set of all the authors having hop distance at most equal to d with the input author. A graph having them as nodes can thus be created and visualized.*

5.__`shortest_path.py`__:
> The packages required: heapq, networkx, collections.
> The last script furnishes two functions based on Dijikstra's algorithm:

> * shortestPath(G, source, target): *it solves the shortest path problem, when a single source and a single target are of interest. An author is chosen by the user and the total weight of the shortest path from him to Aris Anagnostopoulos is returned, provided it exists.* 
> * shortestPath_all(G, q): *this function takes in input the graph G and a set q of nodes of the graph and for each vertex of the networks, it computes the minimum between the shortest path weights from it to any element of I. Clearly, if a node is not connected to any vertex belonging to I, it is not included in the output.*

6.__`HW4.ipynb`__:
> An Ipython Notebook is additionally provided, which contains the entire code, briefly explained as well as the results of the analysis. 

