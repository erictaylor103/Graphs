"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    #Represent a graph as a dictionary of vertices mapping labels to edges.
    def __init__(self):
        self.vertices = {}
    
    #Add a vertex to the graph.
    def add_vertex(self, vertex_id):

        self.vertices[vertex_id] = set()
        print("My Vertex Id: ", vertex_id)
    
    #Add a directed edge to the graph.
    def add_edge(self, v1, v2):

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertice does not exist")
        
    #Get all neighbors (edges) of a vertex.
    def get_neighbors(self, vertex_id):
    
        return self.vertices[vertex_id]

    #Print each vertex in breadth-first order beginning from starting_vertex.
    #BREADTH FIRST TRAVERSAL (uses queue)
    def bft(self, starting_vertex):
        #create an empty queue
        queue = Queue()
        #add starting vertex
        queue.enqueue(starting_vertex)
        #create a set for visited vertices
        visited = set()
        #check to see if queue is not empty
        if queue.size() > 0:
            #Dequeue a vertex
            vertex = queue.dequeue()
        
        #If the vertex has not been visited:
        if vertex not in visited:
            #visit the vertex
            print("Visited Vertex: ", vertex)
            #mark the vertex as visited by adding it to the visited set
            visited.add(vertex)

            #Add all the neighbors of the visited vertex to the queue
            for neighbor in self.get_neighbors(vertex):
                queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #If there is no vertex in the visited set
        if visited is None:
            #Create an empty visited set
            visited = set()
        
        visited.add(starting_vertex)

        print("Starting Vertex: ", starting_vertex)

        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
            print("Visited: ", visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #if the visited set is empty
        if visited is None:
            #create a visited set
            visited = set()
        
        #If there is no path in the path list
        if path is None:
            #create an empty path list
            path = []
        
        #Add the starting vertex to the visited set
        visited.add(starting_vertex)

        #Make a copy of the path
        path = list(path)
        #Add the starting vertex to the path copy
        path.append(starting_vertex)

        #if we've backtracked all the way to the starting vertex return the path to stop recursive traversal
        if starting_vertex == destination_vertex:
            return path
        
        #traverse through the neighbors and check if they have been visited or not
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        
        return None

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("My Graph Vertices: ", graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
