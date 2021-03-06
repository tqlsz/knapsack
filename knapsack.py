# coding:utf-8
import numpy as np
from array import *
import gc
def optimal(k, j, w, v):
    if j == -1:
        return [0, []]
    if w[j] <= k:
        temp1 = optimal(k, j-1, w, v)
        temp2 = optimal(k-w[j], j-1, w, v)
        if temp1[0] > temp2[0] + v[j]:
            temp1[1].append(0)
            return temp1
        else:
            temp2[1].append(1)
            temp2[0] = temp2[0] + v[j]
            return temp2
    else:
        temp1 = optimal(k, j-1, w, v)
        temp1[1].append(0)
        return temp1


def optimal_iteration(capacity, wNumbers, w, v):
    # 用二维数组来表示max[i,j]
    print capacity, wNumbers
    maxV = [[0 for col in range(wNumbers+1)] for row in range(capacity+1)]
    print 'xxxxxxxxxxxxxxxxx1'
    return 0
    for i in range(wNumbers):
        for j in range(0, (capacity+1)):
            if w[i] > j:
                maxV[j][i+1] = maxV[j][i]
            else:
                if maxV[j][i] > v[i] + maxV[j-w[i]][i]:
                    maxV[j][i+1] = maxV[j][i]
                else:
                    maxV[j][i+1] = v[i] + maxV[j-w[i]][i]
            # print 'j,i', j, i+1, maxV[j][i+1]
        col = wNumbers
        row = capacity
        maxIndex = []
        while col > 0:
            if maxV[row][col] > maxV[row][col-1]:
                maxIndex.insert(0, 1)
                row = row - w[col-1]
            else:
                maxIndex.insert(0, 0)
            col -= 1

    return maxV[capacity][wNumbers], maxIndex


class Node():
    def __init__(self, op=0, value=0, capacity=0, index=0, l_child=None, r_child=None):
        '''最优值'''
        self.optimal = op
        '''节点值'''
        self.value = value
        '''节点容量'''
        self.capacity = capacity
        '''记录树的层数'''
        self.index = index
        self.index_w = []
        self.l_child = l_child
        self.r_child = r_child


class Optimal_dps_tree():
    def __init__(self, node=None, capacity=0, w=None, v=None):
        self.root = node
        self.capacity = capacity
        '''重量序列'''
        self.w = w
        self.min_w = min(w)
        '''价值序列'''
        self.v = v
        '''记录解的最大值'''
        self.maxV = 0
        self.max_index = []
        self.deep_tree = len(w)
        '''先对数据按照密度由大到小排序，方便后序计算'''
        self.vw = map(lambda v1, w1, num: [num, v1, w1, float(v1)/w1], v, w, range(self.deep_tree))
        self.vw.sort(lambda x, y: cmp(y[3], x[3]))
        self.vw = np.array(self.vw)

    def add_node(self, node):
        if self.root is None:
            self.root = node
            return

    def get_max_value(self, capacity, index):
        '''weights与values都为数组'''
        '''需要计算从index开始最优值'''
        maxV = 0
        # print index
        if index >= self.deep_tree:
            return 0, 0
        min_w = min(self.vw[index:, 2])
        while index < self.deep_tree:
            if capacity < self.vw[index][2]:
                maxV += capacity*self.vw[index][3]
                break
            else:
                maxV += self.vw[index][1]
                capacity -= self.vw[index][2]
            index += 1
        return maxV, min_w

    def get_maxV_by_w(self, capacity, index):
        '''如果capacity小于最小重量的两倍，找出重量小于capacity，最大v'''
        maxV = 0
        index_w = 0
        while index < self.deep_tree:
            if self.vw[index][2] <= capacity:
                maxV = self.vw[index][1]
                index_w = self.vw[index][0]
                break
            index += 1
        return maxV, index_w

    def recur_create_preorder(self,  root):
        '''通过递归使用合适的节点创建树'''
        if root is None:
            return
        '''需要一系列计算来创造节点'''
        '''满足一定条件才创建左节点，不然返回'''
        capacity = root.capacity
        index = root.index
        if capacity <= 2*min(self.vw[index:, 2]):
            '''算法优化:如果capacity小于重量数组中最小数两倍，则只能选取'''
            '''其中小于capacity，价值最高的v'''
            max_v = self.get_maxV_by_w(capacity, index)
            value = root.value + max_v[0]
            op = value
            root.l_child = Node(op, value, capacity, index+1)
            root.l_child.index_w = root.index_w + [max_v[1]]
            self.maxV = max(self.maxV, value)
            self.max_index = root.l_child.index_w
        else:
            capacity = root.capacity - self.vw[root.index][2]
            if capacity >= 0:
                index = root.index + 1
                max_value = self.get_max_value(capacity, index)
                value = root.value + self.vw[root.index][1]
                op = value + max_value[0]
                if self.maxV < value:
                    self.maxV = value
                    self.max_index = root.index_w + [self.vw[root.index][0]]
                # print 'op', op
                '''如果已经算出的极值小于最优解'''
                if self.maxV <= op:
                    root.l_child = Node(op, value, capacity, index)
                    root.l_child.index_w = root.index_w + [self.vw[root.index][0]]
                    '''根据index来计算最优值'''
                    if root.l_child.index < self.deep_tree:
                        # print 'sdfsdf', capacity, max_value
                        if capacity >= max_value[1]:
                            self.recur_create_preorder(root.l_child)

            '''满足一定条件才能创建右节点，不然返回'''
            capacity = root.capacity
            value = root.value
            index = root.index + 1
            '''计算最优解'''
            max_value = self.get_max_value(capacity, index)
            op = value + max_value[0]
            # print 'op',op
            if self.maxV <= op:
                root.r_child = Node(op, value, capacity, index)
                root.r_child.index_w = root.index_w
                if root.r_child.index < self.deep_tree:
                    # print 'weeee',capacity, max_value
                    if capacity >= max_value[1]:
                        self.recur_create_preorder(root.r_child)

    def recur_preorder_trvalsal(self, root):
        '''递归实现先序遍历'''
        if root is None:
            return
        print root.index_w
        self.recur_preorder_trvalsal(root.l_child)
        self.recur_preorder_trvalsal(root.r_child)


def test():
    v = [8, 10, 15, 4]
    w = [4, 5, 8, 3]
    capacity = 19
    root = Node(0, 0, capacity)
    tree = Optimal_dps_tree(root, capacity, w, v)
    tree.recur_create_preorder(tree.root)
    print '--------------------------'
#    tree.recur_preorder_trvalsal(tree.root)
    print tree.maxV, tree.max_index


if __name__ == '__main__':
    test()
