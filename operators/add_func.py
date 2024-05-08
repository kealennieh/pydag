from core.graph import Node


class AddFunc(Node):
    def __init__(self, **kwargs):
        super(AddFunc, self).__init__(**kwargs)

    def process(self, inputs):
        one_list = inputs["one"]
        two_list = [val + 1 for val in one_list]

        output_dict = {}
        output_dict["two"] = two_list

        return output_dict
