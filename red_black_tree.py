# coding:utf-8
from binary_search_tree import BSTree
from tree import Node

'''定义一个类继承BSTTree'''


class RBTree(BSTree):
    def __init__(self, node=None):
        BSTree.__init__(self, node)


def test():
    rbtree = RBTree()
    import random
    N = 2900
    values = range(N)
    values = random.sample(values, N)
    # values = [15, 5, 4, 2, 3, 0, 13, 1, 18, 11, 8, 7, 17, 9, 12, 14, 16, 6, 10]
    nodes = [Node(el) for el in values]

    print values
    for i in range(N):
        rbtree.add_node(nodes[i])

    rbtree.del_node(nodes[1])
    rbtree.recur_midorder_trvalsal(rbtree.root)


if __name__ == '__main__':
    test()
