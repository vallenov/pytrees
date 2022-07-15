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
            return
        self._passing(self.head_node)

    def _passing(self, current_node: BaseNode):
        if not current_node:
            return
        print(current_node.value)
        self._passing(current_node.left_edge)
        self._passing(current_node.right_edge)

    def _search(self, current_node: BaseNode, value: int):
        if not current_node:
            print('None')
            return
        if current_node.value != value:
            if current_node.left_edge:
                print('left')
                self._search(current_node.left_edge, value)
            elif current_node.right_edge:
                print('right')
                self._search(current_node.right_edge, value)
            else:
                print('None None')
                #current_node.left_edge = BaseNode(value)
                return
        else:
            print('res', current_node)
            return current_node

    def index(self, value: int):
        return self._search(self.head_node, value)

    def append(self, value: int):
        if not self.head_node:
            self.head_node = BaseNode(value)
        else:
            self._append_recursive(self.head_node, value)

    def extend(self, value: list):
        for val in value:
            if not self.head_node:
                self.head_node = BaseNode(val)
            else:
                self._append_recursive(self.head_node, val)

    def remove(self, value: int):
        self._remove_recursive(self.head_node, value)

    def _remove_recursive(self, current_node: BaseNode, value: int):
        if not current_node:
            return
        if not current_node.left_edge:
            return
        if current_node.left_edge.value == value:
            if current_node.left_edge.left_edge:
                current_node.left_edge.value = current_node.left_edge.left_edge.value
                current_node.left_edge.left_edge.right_edge = current_node.left_edge.right_edge
            elif current_node.left_edge.right_edge:
                current_node.left_edge = current_node.left_edge.right_edge
                del current_node.left_edge.right_edge
                return
        self._remove_recursive(current_node.left_edge, value)
        if not current_node.right_edge:
            return
        if current_node.right_edge.value == value:
            if current_node.right_edge.left_edge:
                current_node.right_edge = current_node.right_edge.left_edge
                del current_node.right_edge.left_edge
            elif current_node.right_edge.right_edge:
                current_node.right_edge.value = current_node.right_edge.right_edge.value
                current_node.right_edge.right_edge.left_edge = current_node.right_edge.left_edge
                del current_node.right_edge.left_edge
                return
        self._remove_recursive(current_node.right_edge, value)

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

