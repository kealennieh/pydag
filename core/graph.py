from collections import defaultdict
from toposort import toposort_flatten


NODE_CLASS_DICT = dict()


def registry_node(name, node):
    if name in NODE_CLASS_DICT.keys():
        print("%s is already registerred" % (name))
        return None

    NODE_CLASS_DICT[name] = node


def build_node(name, node_dict):
    if name not in NODE_CLASS_DICT.keys():
        print("%s has not been registerred" % (name))
        return None

    return NODE_CLASS_DICT[name](**node_dict)


class Node:
    def __init__(self, **kwargs):
        super(Node, self).__init__()
        self.name = kwargs["name"]
        self.type = kwargs["type"]
        self.inputs = kwargs.get("inputs", {})
        self.outputs = kwargs.get("outputs", {})

    def process(self, inputs):
        pass


class Graph:
    def __init__(self):
        super(Graph, self).__init__()
        self.idx_to_name_dict = {}
        self.name_to_idx_dict = {}
        self.idx_to_node_dict = {}

    def build_graph(self, graph_file):
        # create node
        for idx, node_val in enumerate(graph_file):
            node = build_node(node_val["type"], node_val)
            if node is None:
                return None

            self.idx_to_name_dict[idx] = node_val["name"]
            self.name_to_idx_dict[node_val["name"]] = idx
            self.idx_to_node_dict[idx] = node

        # analyze the dependency
        dependency_dict = {}
        for idx, node_val in enumerate(graph_file):
            tmp_set = set()

            for dep_val in node_val["deps"]:
                if dep_val not in self.name_to_idx_dict.keys():
                    print(
                        "cannot recognize the deps %s in node %s"
                        % (dep_val, node_val["name"])
                    )
                    return None

                tmp_set.add(self.name_to_idx_dict[dep_val])

            dependency_dict[idx] = tmp_set

        dep_idx_list = list(toposort_flatten(dependency_dict))
        dep_node_list = [self.idx_to_node_dict[val] for val in dep_idx_list]

        return dep_node_list
