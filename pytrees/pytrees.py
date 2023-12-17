import random

from trees.base_tree import BinaryTree


if __name__ == '__main__':
    tr = BinaryTree()
    tr.extend([5, 3, 7, 12, 0, 7, 15])
    tr.print_tree()
    tr.levels_count()
    tr.remove(8)
    tr.print_tree()
    tr.remove(7)
    tr.print_tree()
    tr.append(7)
    tr.print_tree()
    print('---------')
    print(tr.index(20))
    print(tr.index(7))
    print(1 in tr)
    print('---------')
    tr.clear()
    l = list(range(10))
    random.shuffle(l)
    tr.extend(l)
    tr.print_tree()
    tr.clear()
    tr.extend(['qwe', 'rfd', 'tvf', 'cvb', 'zxc'])
    tr.print_tree()
