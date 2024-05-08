from core.graph import Node


class ReadFunc(Node):
    def __init__(self, **kwargs):
        super(ReadFunc, self).__init__(**kwargs)

    def process(self, inputs):
        output_dict = {}
        output_dict["one"] = [1, 3, 5]

        return output_dict
