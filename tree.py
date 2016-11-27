# coding:utf-8

# 类节点


class Node():
    def __init__(self, x=-1, r_child=None, l_child=None):
        self.__x = x
        self.l_child = l_child
        self.r_child = r_child

    def get(self):
        return self.__x

    def set(self, x):
        self.__x = x
# 树类


class Tree():
    # 初始化一棵树
    def __init__(self, node=None):
        self.root = node

    def add_node(self, node):
        my_queue = []
        if self.root is None:
            self.root = node
            return
        temp_node = self.root
        while temp_node:
            if temp_node.l_child is None:
                temp_node.l_child = node
                return
            if temp_node.r_child is None:
                temp_node.r_child = node
                return
            my_queue.append(temp_node.l_child)
            my_queue.append(temp_node.r_child)
            temp_node = my_queue.pop(0)

    def recur_preorder_trvalsal(self, root):
        '''递归实现先序遍历'''
        if root is None:
            return
        print root.get()
        self.recur_preorder_trvalsal(root.l_child)
        self.recur_preorder_trvalsal(root.r_child)

    def stack_preorder_trvalsal(self, root):
        '''堆栈实现先序遍历'''
        stack = []
        temp_node = root
        while temp_node:
            print temp_node.get()
            if temp_node.l_child is not None:
                stack.append(temp_node)
                temp_node = temp_node.l_child
            else:
                if stack == []:
                    return
                temp_node = stack.pop()
                while temp_node.r_child is None:
                    if stack == []:
                        return
                    temp_node = stack.pop()
                temp_node = temp_node.r_child

    def recur_midorder_trvalsal(self, root):
        '''递归实现中序遍历'''
        if root is None:
            return
        self.recur_midorder_trvalsal(root.l_child)
        print root.get()
        self.recur_midorder_trvalsal(root.r_child)

    def stack_midorder_trvalsal(self, root):
        '''堆栈实现中序遍历'''
        temp_node = root
        my_stack = []
        while temp_node or my_stack:
            if temp_node is not None:
                my_stack.append(temp_node)
                temp_node = temp_node.l_child
            else:
                temp_node = my_stack.pop()
                print temp_node.get()
                temp_node = temp_node.r_child
        '''
        while temp_node:
            if temp_node.l_child:
                my_stack.append(temp_node)
                temp_node = temp_node.l_child
            else:
                print temp_node.get()
                if my_stack == []:
                    return
                temp_node = my_stack.pop()
                print temp_node.get()
                while temp_node.r_child is None:
                    if my_stack == []:
                        return
                    temp_node = my_stack.pop()
                    print temp_node.get()
                temp_node = temp_node.r_child
        '''
    def recur_postorder_trvalsal(self, root):
        '''递归实现后序遍历'''
        if root is None:
            return
        self.recur_postorder_trvalsal(root.l_child)
        self.recur_postorder_trvalsal(root.r_child)
        print root.get()

    def stack_postorder_trvalsal(self, root):
        '''堆栈实现后序遍历'''
        my_stack1 = []
        my_stack2 = []
        temp_node = root
        while temp_node or my_stack1:
            if temp_node:
                my_stack2.append(temp_node)
                my_stack1.append(temp_node)
                temp_node = temp_node.r_child
            else:
                temp_node = my_stack1.pop()
                temp_node = temp_node.l_child
        while my_stack2:
            print my_stack2.pop().get()


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add_node(Node(i))
    tree.stack_postorder_trvalsal(tree.root)
