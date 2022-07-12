class BaseNode:
    def __init__(self, value, right_edge=None, left_edge=None):
        self.value = value
        self.right_edge = right_edge
        self.left_edge = left_edge

    def __repr__(self):
        return f'<{type(self).__name__} {self.value} (left: {self.left_edge}, right: {self.right_edge})>'

    def copy(self):
        return BaseNode(value=self.value,
                        right_edge=self.right_edge,
                        left_edge=self.left_edge)


class BinaryTree:
    def __init__(self):
        self.head_node = None
        self.level_count = 1

    def print_tree(self):
        if not self.head_node:
            print('Tree is empty')
        self._passing(self.head_node)

    def _passing(self, current_node: BaseNode):
        if not current_node:
            return
        print(current_node.value)
        self._passing(current_node.left_edge)
        self._passing(current_node.right_edge)

    def append(self, value: int):
        if not self.head_node:
            self.head_node = BaseNode(value)
        else:
            self._append_recursive(self.head_node, value)

    def _append_recursive(self, current_node: BaseNode, value: int):
        if current_node.value > value:
            if current_node.left_edge:
                self._append_recursive(current_node.left_edge, value)
            else:
                current_node.left_edge = BaseNode(value)
                return
        else:
            if current_node.right_edge:
                self._append_recursive(current_node.right_edge, value)
            else:
                current_node.right_edge = BaseNode(value)
                return

