############################################################################################
#                                  Author: Anas AHOUZI                                     #
#                               File Name: Trees_and_graphs.py                             #
#                           Creation Date: August 31, 2020                                 #
#                         Source Language: Python                                          #
#     Repository: https://github.com/aahouzi/Algorithms-and-Data-Structures-in-Python      #
#                              --- Code Description ---                                    #
#                       Implementation of trees & graphs in Python                         #
############################################################################################


################################################################################
#                                   Packages                                   #
################################################################################

from collections import defaultdict
import sys

################################################################################
#                         Implementation of a tree                             #
################################################################################


class Node:
    def __init__(self, data, left, right):
        """
        This function is for intializing the tree.
        :param data: A scalar.
        :param left: A Node class in the left side of data.
        :param right: A Node class in the right side of data.
        """
        self.Left = left
        self.Right = right
        self.data = data

    def print_tree(self):
        """
        This function prints all the elements of a tree, from the left
        side, center and then the right side.
        :return:
        """

        if self.Left:
            self.Left.print_tree()

        if self.data is not None:
            print(self.data)

        if self.Right:
            self.Right.print_tree()

    def insert(self, elt):
        """
        This function inserts an element in the correct position in a binary tree.
        :param elt: The element to insert.
        :return:
        """

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
        """
        This function looks for an element in a binary tree.
        :param elt: The element to look for.
        :return:
        """

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
        """
        This function looks for the minimum element in a binary tree.
        :return: The minimum of a binary tree.
        """

        if self.Left is None:
            return self.data
        else:
            return self.Left.min_tree()

    def delete(self, elt):
        """
        This function deletes an element from a binary tree.
        :param elt: The element to be deleted.
        :return:
        """

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
        """
        :return: This function returns the 10-weighted sum of all
        paths in the tree from the root to the leaf.
        """

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


################################################################################
#                         Implementation of a graph                            #
################################################################################


class Graph():
    def __init__(self):
        """
        We will initialize the graph as a defaultdict, where every key
        is a vertex, whose value is a list containing adjacent vertices.
        """
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        :param u: An existing vertex.
        :param v: A new vertex, that we connect with the existing one
        by adding it to the list of u.
        :return:
        """
        self.graph[u].append(v)

    def bfs(self, s):
        """
        This is an implementation of Breadth First Search, where we start from a certain vertex s in the
        graph, and we print its adjacent vertices. We continue the same process until all the vertices are
        explored.
        :param s: The starting vertex.
        :return:
        """

        # Initializing a vector to mark visited vertices
        V = [False] * len(self.graph)

        # Mark the source node as visited and enqueue it
        queue = self.graph[s]
        V[s] = True
        print("{} \n".format(s))

        while queue:

            # Get the first vertex in queue
            k = queue.pop(0)

            # Check whether vertex k was visited. If not, print it and extend
            # the original list of s, with adjacent vertices of k, and then
            # finally mark vertex k as visited.
            if not V[k]:
                print("{} \n".format(k))
                queue.extend(self.graph[k])
                V[k] = True

    def dfs_int(self, s, V):

        V[s] = True
        print("{} \n".format(s))

        for i in self.graph[s]:
            if not V[i]:
                self.dfs_int(i, V)

    def dfs(self, s):
        """
        This is an implementation of Depth First Search, where we start from a certain vertex s,
        and we explore an adjacent unvisited vertex as far as possible, before we start backtracking.
        :param s: The starting vertex.
        :return:
        """

        V = [False] * len(self.graph)
        self.dfs_int(s, V)


################################################################################
#          Implementation of Dijkstra's Shortest Path algorithm                #
################################################################################

class shortest_path():
    def __init__(self, num_vertex, adjacendy_mat):
        """
        The graph is initialized with an adjacency matrix containing the weight
        values of edges connecting every two vertices, and the number of vertices,
        which is also the size of the adjacency matrix.
        :param num_vertex: Number of vertices in the graph.
        :param adjacendy_mat: The adjacency matrix.
        """
        self.v = num_vertex
        self.mat = adjacendy_mat

    def min_dist(self, visited, dist):
        """
        This function returns the vertex having the minimum distance from the source vertex,
        and which is not yet visited by the algorithm.
        :param visited: A list of boolean values.
        :param dist: A list of each vertex distance from the source vertex.
        :return:
        """

        min_ind = 0
        m = sys.maxsize

        for i in range(self.v):
            if dist[i] < m and not visited[i]:
                m = dist[i]
                min_ind = i

        return min_ind

    def print_dist(self, dist):

        for i in range(self.v):
            print("Distance to {}: {}".format(i, dist[i]))

    def djikstra(self, src):
        """
        Starting from a certain vertex src, we wanna know what is the shortest
        distance to every other vertex in the graph.
        :param src: The starting vertex.
        :return:
        """

        # A list to mark visited vertices.
        V = [False] * self.v
        # A list containing distances from the vertex src, to all other vertices.
        dist = [sys.maxsize] * self.v
        # The distance for src is 0.
        dist[src] = 0

        # We loop through the number of vertices, and at each iteration we
        # pick the vertex having the minimum distance from src vertex.
        for i in range(self.v):

            u = self.min_dist(V, dist)
            V[u] = True

            for j in range(self.v):
                # First, we check whether there's an edge connecting the vertex
                # u with the vertex j (mat[u][j] != 0), and then we check if the
                # vertex j is not already visited. Finally, if the previous conditions
                # are verified, we check if u vertex's distance plus the edge weight
                # connecting u and j is smaller than the j vertex's distance
                if self.mat[u][j] != 0 and not V[j] and dist[u] + self.mat[u][j] < dist[j]:
                    dist[j] = dist[u] + self.mat[u][j]

        self.print_dist(dist)


adjecendy_mat = [[0, 3, 2, 0, 0],
                 [3, 0, 0, 1, 5],
                 [2, 0, 0, 6, 0],
                 [0, 1, 6, 0, 1],
                 [0, 5, 0, 1, 0]]

num_vertex = 5
dji = shortest_path(num_vertex, adjecendy_mat)
dji.djikstra(0)
