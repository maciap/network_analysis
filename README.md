# HW4-ADM-GROUP26
Network analysis

The scripts proposed in this repository solve the exercises in Homework 4, Algorithmic Methods for Data Mining, Master's degree in Data Science, Sapienza University of Rome. 

## Data

The data in usage is the DBLP data set. It contains information concerning Computer Science academic publications, in json format.  
In particular, not only the complete but also a reduced version of the data set are taken into account. 
The user is allowed to choose the data to be analysed. 

## Script descriptions

1. __`main.py`__:
> This module calls the functions contained in the scripts below in orded to tidily present the results of the exercises given in 
[Homework 4](http://aris.me/contents/teaching/data-mining-ds-2017/homeworks/homework4.pdf). The user may be prompted for input.

2. __`graph.py`__:
> This module provides the code necessary in order to load the chosen data set and creates a graph to model them. 
>	Four functions are provided:
>  * choose_data: *the user is prompted to choose the complete or reduced data set.*
>  * import_data: *the desired data set is returned.*
>  * create_graph: *the graph is retuned.*
>  * plot_graph: *the graph is plotted.*

3.__`centrality.py`__:
> This script contains functions that allows to compute and visualize different centrality measures associated with each node in the 
> graph. The following procedures are defined:

>* bar_plot_degree: *it displays a bar chart of the node degrees.*
>* compute_centrality_measures: *Four measures for each node, namely degree, betweeness, closeness and eigenvector centrality, are computed.*
> * bar_plot: *A bar chart useful in order to visually assess every centrality measure is obtained.*
> * strip_plot: *A strip-plot is built as an alternative to the bar-chart.* 
> * centrality_measures_plot: *The code of this function displays a plot including a bar chart and a strip-plot for each centrality measure.*
> * scatterplot_matrix: *A scatterplot matrix is built. This is useful when the aim is exploring the relationship between the different centrality measures. On the main diagonal, histograms are displayed, which is appropriate only when the number of distinct values of the measures is not extremely low.*

4.__`hop_distance.py`__:
> This file is composed by a single function: 
> *hop_d: *this is a recursive function that, given author and an integer **_d_**, returns the set of all the authors having hop distance at most equal to **_d_** with the input author. A graph having them as nodes can thus be created and visualized.*

5.__`shortest_path.py`__:
> The last script furnishes two functions based on Dijikstra's algorithm.
> * shortestPath: *it solves the shortest path problem, when a single source and a single target are of interest. An author is chosen by the user and the total weight of the shortest path from him to Aris Anagnostopoulos is returned, provided it exists.* 
> * shortestPath_all: *This function takes in input a set I of nodes of the graph and for each vertex of the networks, it computes the minimum between the shortest path weights from it to any element of I. Clearly, if a node is not connected to any vertex belonging to I, it is not included in the output.*

6.__`HW4.ipynb`__:
> An Ipython Notebook is additionally provided, which contains the entire code, briefly explained as well as the results of the analysis.  

