class BaseNode:
    def __init__(self, value, right_edge=None, left_edge=None):
        self.value = value
        self.right_edge = right_edge
        self.left_edge = left_edge

    def __repr__(self):
        return f'<{type(self).__name__} {self.value} (left: {self.left_edge}, right: {self.right_edge})>'
