# coding:utf-8
import tree
'''
二叉排序树或者是一棵空树，或者是具有下列性质的二叉树：
（1）若左子树不空，则左子树上所有结点的值均小于或等于它的根结点的值；
（2）若右子树不空，则右子树上所有结点的值均大于或等于它的根结点的值；
（3）左、右子树也分别为二叉排序树；
 (4) 没有键值相等的节点
'''

'''定义一个类继承Tree类'''


class BSTree(tree.Tree):
    def __init__(self, node=None):
        tree.Tree.__init__(self, node)

    def add_node(self, node):
        '''向树中添加节点，也就是构建树
        1.如果根节点为空，创建根节点
        2.将加入节点值与根节点比较，大了放右节点，小了放左节点
        '''
        if self.root is None:
            self.root = node
            return
        temp = self.root
        node_val = node.get()
        while temp:
            temp_val = temp.get()
            if node_val > temp_val:
                if temp.r_child:
                    temp = temp.r_child
                else:
                    temp.r_child = node
                    return
            elif node_val <= temp_val:
                if temp.l_child:
                    temp = temp.l_child
                else:
                    temp.l_child = node
                    return

    def del_node(self, node):
        '''首先找到node节点'''
        temp = self.root
        node_val = node.get()
        father_node = None
        while temp:
            temp_val = temp.get()
            if node_val == temp_val:
                '''找到节点'''
                if temp.l_child is None and temp.r_child is None:
                    '''叶节点，直接删除'''
                    if father_node is None:
                        '''temp is root'''
                        self.root = None
                    else:
                        if father_node.l_child == temp:
                            father_node.l_child = None
                        else:
                            father_node.r_child = None
                elif temp.l_child is None:
                    if father_node.l_child == temp:
                        father_node.l_child = temp.r_child
                    else:
                        father_node.r_child = temp.r_child
                    temp = None
                elif temp.r_child is None:
                    if father_node.l_child == temp:
                        father_node.l_child = temp.l_child
                    else:
                        father_node.r_child = temp.r_child
                    temp = None
                else:
                    right_node = temp.l_child
                    father_right_node = None
                    '''查找用左子树的最右边节点代替删除的节点'''
                    while right_node.r_child:
                        father_right_node = right_node
                        right_node = right_node.r_child
                    if father_node.l_child == temp:
                        father_node.l_child = right_node
                    else:
                        father_node.r_child = right_node
                    if father_right_node is not None:
                        father_right_node.r_child = right_node.l_child
                    right_node.l_child = temp.l_child
                    right_node.r_child = temp.r_child
                    temp = None
                return
            elif node_val < temp_val:
                father_node = temp
                temp = temp.l_child
            else:
                father_node = temp
                temp = temp.r_child


def test():
    bstree = BSTree()
    import random
    values = range(19)
    values = random.sample(values, 19)
    values = [15, 5, 4, 2, 3, 0, 13, 1, 18, 11, 8, 7, 17, 9, 12, 14, 16, 6, 10]
    nodes = [tree.Node(el) for el in values]
    print values
    for i in range(19):
        bstree.add_node(nodes[i])

    bstree.del_node(nodes[1])

    bstree.recur_midorder_trvalsal(bstree.root)
if __name__ == '__main__':
    test()
