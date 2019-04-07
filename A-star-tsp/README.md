# A-star-TSP

## 1. maze.txt defines a maze, 
@ represents the check point you need to pass through, 
. means the space area, 
'#' means the wall, 
S is the start point, 
G is the goal point.
Your goal is to figure out the shortest way starting at S, passing through all @(check points), and finally getting to the goal point G.

The basic thinking is using A* algorithm generates the shortest path between each points in (S, G and all @).
Then it becomes the TSP problem.
And we can use Simulating Anealing algorithm and Dynamic Programming to solve it.

A* algorithm and Traval Salesman Problem using Dynamic Programming and Simulating Anealing algorithm

## 2. node.py
	defines the class Node

## 3. AStar.py
	runs the A* algorithm on the maze.txt
	generates a distance matrix for doing TSP
## 4. TSP_DP.py
	runs TSP problem using Dynamic Programming-- when N (the number of @ check points) < 10, Dynamic Programming if faster than Simulating Anealing algorithm
## 5. TSP_SA.py
	runs TSP problem using Simulating Anealing algorithm.