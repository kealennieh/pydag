from core.graph import registry_node
from .read_func import ReadFunc
from .add_func import AddFunc

registry_node("ReadFunc", ReadFunc)
registry_node("AddFunc", AddFunc)
