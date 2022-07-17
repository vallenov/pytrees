import time


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
        self.max_len_value = 0

    def print_tree(self):
        if not self.head_node:
            print('Tree is empty')
            return
        self._passing_draw()
        print(f'Levels count: {self.levels_count()}\n')

    def levels_count(self):
        level_count = 0
        if not self.head_node:
            return level_count
        lst = [self.head_node]
        while lst:
            level_count += 1
            tmp = lst.copy()
            lst = []
            for node in tmp:
                if node.left_edge:
                    lst.append(node.left_edge)
                if node.right_edge:
                    lst.append(node.right_edge)
        return level_count

    def clear(self):
        self.head_node = None

    def _passing(self, current_node: BaseNode):
        if not current_node:
            return
        print(current_node.value)
        self._passing(current_node.left_edge)
        self._passing(current_node.right_edge)

    def _passing_draw(self):
        """
        Beautiful tree drawing
        """
        lst = [self.head_node]
        lev_tree = self.levels_count()
        width = (2 ** lev_tree + 1) * (self.max_len_value + 1)
        cur_level = 1
        while lst:
            string = f'level {cur_level}:'.ljust(10)
            interval = width // len(lst)
            for node in lst:
                if node is None:
                    val = 'N'
                elif node == '':
                    val = ''
                else:
                    val = node.value
                string += f'{val}'.center(interval)
            print(string)
            cur_level += 1
            tmp = lst.copy()
            lst = []
            for node in tmp:
                if not node or node == '':
                    lst.extend(['', ''])
                    continue
                if node.left_edge:
                    lst.append(node.left_edge)
                else:
                    lst.append(None)
                if node.right_edge:
                    lst.append(node.right_edge)
                else:
                    lst.append(None)
            if lst.count('') == len(lst):
                break

    def _search(self, current_node: BaseNode, value: int):
        if not current_node:
            return
        if current_node.value != value:
            if current_node.left_edge:
                self._search(current_node.left_edge, value)
            elif current_node.right_edge:
                self._search(current_node.right_edge, value)
            return
        else:
            print(current_node.value)
            return current_node.value

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
                current_node.left_edge = current_node.left_edge.left_edge
            elif current_node.left_edge.right_edge:
                current_node.left_edge.right_edge.left_edge = current_node.left_edge.left_edge
                current_node.left_edge = current_node.left_edge.right_edge
            else:
                current_node.left_edge = None
            return
        self._remove_recursive(current_node.left_edge, value)
        if not current_node.right_edge:
            return
        if current_node.right_edge.value == value:
            if current_node.right_edge.left_edge:
                current_node.right_edge.left_edge.right_edge = current_node.right_edge.right_edge
                current_node.right_edge = current_node.right_edge.left_edge
            elif current_node.right_edge.right_edge:
                current_node.right_edge.value = current_node.right_edge.right_edge.value
                current_node.right_edge.right_edge.left_edge = current_node.right_edge.left_edge
                current_node.right_edge = current_node.right_edge.right_edge
            else:
                current_node.right_edge = None
            return
        self._remove_recursive(current_node.right_edge, value)

    def _append_recursive(self, current_node: BaseNode, value: int):
        if current_node.value > value:
            if current_node.left_edge:
                self._append_recursive(current_node.left_edge, value)
            else:
                if len(str(value)) > self.max_len_value:
                    self.max_len_value = len(str(value))
                current_node.left_edge = BaseNode(value)
                return
        else:
            if current_node.right_edge:
                self._append_recursive(current_node.right_edge, value)
            else:
                if len(str(value)) > self.max_len_value:
                    self.max_len_value = len(str(value))
                current_node.right_edge = BaseNode(value)
                return

