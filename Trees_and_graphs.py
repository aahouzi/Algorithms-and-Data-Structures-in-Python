############################################################################################
#                                  Author: Anas AHOUZI                                     #
#                               File Name: Trees_and_graphs.py                             #
#                           Creation Date: August 31, 2020                                 #
#                         Source Language: Python                                          #
#     Repository: https://github.com/aahouzi/Algorithms-and-Data-Structures-in-Python      #
#                              --- Code Description ---                                    #
#                       Implementation of trees & Graphs in Python                         #
############################################################################################

from collections import defaultdict
import sys


class Node:
    def __init__(self, data, left, right):
        self.Left = left
        self.Right = right
        self.data = data

    def print_tree(self):

        if self.Left:
            self.Left.print_tree()

        if self.data is not None:
            print(self.data)

        if self.Right:
            self.Right.print_tree()

    def insert(self, elt):

        if self.data >= elt:
            if self.Left is None:
                self.Left = Node(elt, None, None)
            else:
                self.Left.insert(elt)

        elif self.data < elt:
            if self.Right is None:
                self.Right = Node(elt, None, None)
            else:
                self.Right.insert(elt)

    def search(self, elt):

        if elt == self.data:
            print("Found")

        elif self.data > elt:
            if self.Left is None:
                print("Not Found")
            elif self.Left.data == elt:
                print("Found")
            else:
                self.Left.search(elt)

        else:
            if self.Right is None:
                print("Not Found")
            elif self.Right.data == elt:
                print("Found")
            else:
                self.Right.search(elt)

    def min_tree(self):

        if self.Left is None:
            return self.data
        else:
            return self.Left.min_tree()

    def delete(self, elt):

        if elt < self.data:
            if self.Left == Node(elt, None, None):
                self.Left = None
            else:
                self.Left.delete(elt)

        elif elt > self.data:
            if self.Right == Node(elt, None, None):
                self.Right = None
            else:
                self.Right.delete(elt)

        elif elt == self.data:
            if self.Right is None and self.Left is not None:
                self.data = self.Left.data
                self.Left = self.Left.Left
                self.Right = self.Left.Right

            elif self.Left is None and self.Right is not None:
                self.data = self.Right.data
                self.Left = self.Right.Left
                self.Right = self.Right.Right

            elif self.Left is None and self.Right is None:
                self.data = None

            else:
                var = self.Right.min_tree()
                self.Right.delete(var)
                self.data = var

    def sum_root_path(self):

        if self.Right is not None and self.Left is not None:
            self.Left.data += self.data * 10
            self.Right.data += self.data * 10
            return self.Left.sum_root_path() + self.Right.sum_root_path()

        elif self.Right is not None and self.Left is None:
            self.Right.data += self.data * 10
            return self.Right.sum_root_path()

        elif self.Right is None and self.Left is not None:
            self.Left.data += self.data * 10
            return self.Left.sum_root_path()

        else:
            return self.data


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):

        visited = [False] * len(self.graph)

        # Mark the source node as
        # visited and enqueue it
        queue = self.graph[s]
        visited[s] = True
        print(s, end=" ")

        while queue:

            # Dequeue a vertex from
            # queue and print it
            k = queue.pop(0)

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            if not visited[k]:
                print(k, end=" ")
                queue.extend(self.graph[k])
                visited[k] = True

    def DFS_int(self, s, visited):

        visited[s] = True
        print(s, end=" ")

        for i in self.graph[s]:
            if not visited[i]:
                self.DFS_int(i, visited)

    def DFS(self, s):

        visited = [False] * len(self.graph)

        self.DFS_int(s, visited)


class djikstra_graph():

    def __init__(self, num_vertex, adjecendy_mat):
        self.v = num_vertex
        self.mat = adjecendy_mat

    def min_dist(self, visited, dist):

        min_ind = 0
        m = sys.maxsize

        for i in range(self.v):
            if dist[i] < m and not visited[i]:
                m = dist[i]
                min_ind = i

        return min_ind

    def print_dist(self, dist):

        for i in range(self.v):
            print(i, "t", dist[i])

    def djikstra(self, src):

        visited = [False] * self.v
        dist = [sys.maxsize] * self.v
        dist[src] = 0

        for i in range(self.v):

            u = self.min_dist(visited, dist)
            visited[u] = True

            for j in range(self.v):
                if self.mat[u][j] != 0 and not visited[j] and dist[u] + self.mat[u][j] < dist[j]:
                    dist[j] = dist[u] + self.mat[u][j]

        self.print_dist(dist)



g = djikstra_graph(9, adjecendy_mat)
g.djikstra(0)






