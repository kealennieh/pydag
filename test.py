from utils.io_file import load_json_file
from core.pipeline import Pipeline


def test():
    json_file_path = "configs/test.json"
    json_file = load_json_file(json_file_path)

    pipe = Pipeline()
    pipe.build_graph(json_file)
    pipe.process()


if __name__ == "__main__":
    test()
