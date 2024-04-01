from Vertex import Vertex
from Edge import Edge

# At the moment the graph breaks when trying to 
# add an edge to a given vertex. It believes that the vertex object is a list
# and needs some help

class Graph(Vertex):
    def __init__(self, vertices:list):
        self.vertices = vertices

    def add_vertex(self, vertex_input_data):
        "Method docstring to be composed"
        newV = Vertex(vertex_input_data)
        self.vertices.append(newV)
        return newV
    
    def remove_vertex(self,vertex:Vertex):
        self.vertices.remove(vertex)
    
    def add_edge(self, vertex1:Vertex, vertex2:Vertex, weight):
        "Method docstring to be composed"
        to = vertex1.add_edge(vertex2, weight)
        fro = vertex2.add_edge(vertex1, weight)
        return to, fro
    
    def remove_edge(self, vertex1:Vertex, vertex2:Vertex):
        "Method docstring to be composed"
        vertex1.remove_edge(vertex2)
        vertex2.remove_edge(vertex1)
    

def test_graph():
    my_graph = Graph(list())
    my_graph.add_vertex("vertex one")
    my_graph.add_vertex("vertex two")
    my_graph.add_vertex("vertex three")
    my_graph.add_edge(my_graph.vertices[0],my_graph.vertices[1], 1)
    my_graph.add_edge(my_graph.vertices[0],my_graph.vertices[2], 2)
    my_graph.add_edge(my_graph.vertices[1],my_graph.vertices[2], 3)
    for i in my_graph.vertices:
        i.debug_print()

test_graph()