# coding:utf-8

# 类节点


class Node():
    def __init__(self, x=-1,index = 0, r_child=None, l_child=None):
        self.__x = x
        self.index = index
        self.l_child = l_child
        self.r_child = r_child

    def get(self):
        return self.__x

    def setx(self, x):
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

    def get_deep(self, total):
            fac = 1
            total = total+1
            times = 0
            while fac <= total:
                fac = 2*fac
                times = times + 1
            return times

    def create_by_preorder(self, capacity):
            '''将capacity数组按照先序创建二叉树'''
            length = len(capacity)
            if length <= 0:
                return None
            '''计算可以创建树的深度－层数'''
            deep_nums = self.get_deep(length)
            self.root = Node(capacity[0])
            if length == 1:
                return
            '''先在来根据二叉树来估算左右元素个数'''
            '''计算最下层个数bottom_numers'''
            temp = pow(2, (deep_nums-1))
            bottom_numers = length - (temp-1)
            left_numbers = 0
            '''计算左右各占几个数'''
            if bottom_numers >= temp/2:
                left_numbers = temp-1
            else:
                left_numbers = temp-1 - (temp/2-bottom_numers)
            left_capacity = capacity[1:(left_numbers+1)]
            left_tree = Tree()
            right_tree = Tree()
            left_tree.create_by_preorder(left_capacity)
            self.root.l_child = left_tree.root
            right_capacity = capacity[(left_numbers+1):]
            right_tree.create_by_preorder(right_capacity)
            self.root.r_child = right_tree.root

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

    def queue_trvalsal(self, root):
        temp_node = root
        my_stack = []
        while temp_node or my_stack:
            if temp_node:
                print temp_node.get()
                if temp_node.l_child:
                    my_stack.append(temp_node.l_child)
                if temp_node.r_child:
                    my_stack.append(temp_node.r_child)
            if my_stack == []:
                return
            temp_node = my_stack.pop(0)

    def create_preorder(self, deep_nums):
        if self.root is None:
            self.root = Node(0)
        left_tree = Tree()
        left_tree.root = Node(1)
        left_tree.root.index = self.root.index + 1
        if left_tree.root.index > deep_nums:
            return
        left_tree.create_preorder(deep_nums)
        self.root.l_child = left_tree.root
        right_tree = Tree()
        right_tree.root = Node(0)
        right_tree.root.index = self.root.index + 1
        right_tree.create_preorder(deep_nums)
        self.root.r_child = right_tree.root

    def create_preorder1(self, root, deep_nums):
        root.l_child = Node(1)
        root.l_child.index = root.index+1
        if root.l_child.index < deep_nums:
            self.create_preorder1(root.l_child, deep_nums)
        root.r_child = Node(0)
        root.r_child.index = root.index+1
        if root.r_child.index < deep_nums:
            self.create_preorder1(root.r_child, deep_nums)

def test():
    print 'test'

if __name__ == '__main__':
    test()
    print "sdfsdfsdfsd"
    while 1:
        print '1'
