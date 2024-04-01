from Edge import Edge

class Vertex(Edge):
    def __init__(self, data):
        self.data = data
        self.edges = []

    def add_edge(self, end_vertex, weight):
        "Adds an edge to the vertex"
        self.edges.append(Edge(self, end_vertex, weight))

    def remove_edge(self,end_vertex):
        "removes an edge from the vertex"
        self.edges.remove(Edge.get_end(end_vertex))

    def get_data(self):
        "Method docstring to be composed"
        return self.data

    def get_edges(self):
        "Method docstring to be composed"
        return self.edges
    
    def debug_print(self):
        "Method docstring to be composed"
        message = " ".join(f'{self.edges},')
        print(f'vertex name: {self.data} -> debug print')

        for edge in self.edges:
            print(f'{edge.get_start().get_data()} -> {edge.get_end().get_data()}')

        print("END OF VERTEX \n")
        print("________________")
            




