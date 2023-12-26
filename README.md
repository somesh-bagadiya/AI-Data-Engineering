## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [Directory Description](#directory-description)

## Introduction

This repository contains implementations of path-finding algorithms like Dijkstra's, A-Star, RRT, and RRT Star.

## Prerequisites

Basic understanding of all the algorithms mentioned above.

## Setup Instructions

Ensure that Python is installed on your system, and also make sure to install the following libraries: numpy.

## Usage

Visit the folder dedicated to each algorithm and review the associated Python code. Within each folder, you'll find "coords.txt" and "input.txt" files containing obstacle coordinates in a 2D plane. Additionally, each algorithm's code will produce an "output.txt" file, showcasing the coordinates of the shortest path determined by the algorithm.

## Directory Description

### Dijkstra's Algorithm

Dijkstra's algorithm, named after computer scientist Edsger Dijkstra, is a fundamental pathfinding algorithm widely used in computer science and network routing. Designed to find the shortest path between two nodes in a weighted graph, the algorithm traverses the graph iteratively, assigning tentative distances to all nodes and continually updating them as it discovers shorter paths. By the end of its execution, Dijkstra's algorithm provides the shortest path from a specified source node to all other nodes in the graph. Notably efficient for non-negative edge weights, Dijkstra's algorithm has applications in various fields, including transportation networks, telecommunications, and computer networking.

Output of the algorithm:

![Dijkstra's Algorithm](Dijkstra's%20Algorithm/Dijkstra's%20Output.gif)

<img src="Dijkstra's%20Algorithm/dijkstras.png" alt="Dijkstra's Algorithm" width="700" height="469"/>

*Caption: Dijkstra's Algorithm*

### A-Star Algorithm

A* (pronounced "A-star") is a widely used pathfinding algorithm in computer science, commonly employed to find the shortest path between two points in a graph. Developed by Peter Hart, Nils Nilsson, and Bertram Raphael in 1968, A* combines the advantages of both Dijkstra's algorithm and greedy best-first search. It intelligently explores the graph by considering both the cost incurred so far and an estimated cost to reach the goal, determined using a heuristic function.

Weighted A* is a variant of the A* algorithm that introduces the concept of edge weights. While A* traditionally assumes equal costs for all edges, Weighted A* assigns different weights to edges, allowing for more nuanced and realistic representations of real-world scenarios. This modification provides greater flexibility in pathfinding, as it accommodates varying degrees of cost associated with traversing different edges.

Both A* and Weighted A* have found applications in diverse fields, including robotics, video games, and network routing, due to their efficiency in finding optimal paths in complex and dynamic environments.
Output of the algorithm:

![A-Star Algorithm](A-Star%20Algorithm/A-Star%20Output.gif)

<img src="A-Star%20Algorithm/A-star.png" alt="Dijkstra's Algorithm" width="700" height="469"/>

*Caption: Dijkstra's Algorithm*

