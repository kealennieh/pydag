
from core.graph import Graph


class Pipeline():
    def __init__(self):
        super(Pipeline, self).__init__()

    def build_graph(self, graph_file):
        self.graph = Graph()
        self.graph.build_graph(graph_file)

    def process(self):
        pass
