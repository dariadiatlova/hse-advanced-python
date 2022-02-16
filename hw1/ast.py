import ast
import networkx as nx
import inspect

from hw1 import HW_1_ROOT_PATH
from hw1.fibonacchi import get_n_fibonacci_number


class AssignmentVisitor(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        self.graph = nx.DiGraph()
        self.parent = None

    def _get_label(self, node):
        label = None
        try:
            label = str(node.op).split()[0][5:]
        except AttributeError:
            try:
                label = node.value
            except AttributeError:
                try:
                    label = node.id
                except AttributeError:
                    pass
        return label

    def generic_visit(self, node):
        label = self._get_label(node)

        if label:
            self.graph.add_node(str(node), label=label)
        else:
            self.graph.add_node(str(node))

        if self.parent:
            self.graph.add_edge(self.parent, str(node))
        self.parent = str(node)
        super().generic_visit(node)


def main(image_path: str = f"{HW_1_ROOT_PATH}/artifacts/ast.png"):
    tree = AssignmentVisitor()
    function_text = inspect.getsource(get_n_fibonacci_number)
    module = ast.parse(source=function_text)
    tree.visit(module)
    p = nx.drawing.nx_pydot.to_pydot(tree.graph)
    p.write_png(image_path)


# if __name__ == "__main__":
#     main()
