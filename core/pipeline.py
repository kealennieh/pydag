"""
1.init the node and graph
2.analyze the dependency of each node
3.call the process

"""

import operators
from core.graph import Graph
from core.data_table import DataPool


class Pipeline:
    def __init__(self):
        super(Pipeline, self).__init__()
        self.graph = Graph()
        self.data_pool = DataPool()

    def build_graph(self, graph_file):
        self.execute_node_list = self.graph.build_graph(graph_file)

    def process(self):  # single thread
        for node in self.execute_node_list:
            # get input data from data pool
            input_dict = {}
            for input_name in node.inputs:
                table_name, field_name = node.inputs[input_name].split(".")
                input_val = self.data_pool.get_field(table_name, field_name)
                input_dict[input_name] = input_val

            # process
            output_dict = node.process(input_dict)

            # set output data to data pool
            for output_name in node.outputs:
                table_name, field_name = node.outputs[output_name].split(".")

                output_val = output_dict[output_name]
                self.data_pool.add_field(table_name, field_name, output_val)

        print(self.data_pool.table_dict["tb"].df)
        print("well done")
