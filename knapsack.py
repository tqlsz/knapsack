# coding:utf-8


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
    def __init__(self, op=0,  value=0, capacity=0, index=0, l_child=None, r_child=None):
        '''最优值'''
        self.optimal = op
        '''节点值'''
        self.value = value
        '''节点容量'''
        self.capacity = capacity
        '''记录树的层数'''
        self.index = index
        self.l_child = l_child
        self.r_child = r_child


class Optimal_dps_tree():
    def __init__(self, node=None, capacity=0, w=None, v=None):
        self.root = node
        self.capacity = capacity
        '''重量序列'''
        self.w = w
        '''价值序列'''
        self.v = v
        '''记录解的最大值'''
        self.maxV = 0
        self.deep_tree = len(w)

    def add_node(self, node):
        if self.root is None:
            self.root = node
            return

    def get_max_value(self, capacity, weights, values):
        '''weights与values都为数组'''
        '''需要计算values/weights并且从大到小排序'''
        len1 = len(weights)
        len2 = len(values)
        if len1 != len2:
            return
        vw = map(lambda v1, w1: (v1, w1), values, weights)
        vw.sort(lambda x, y: cmp(x[1]*0.1*10/x[0], y[1]*0.1*10/y[0]))
        maxV = 0
        for i in range(len1):
            if capacity < vw[i][1]:
                maxV += capacity*0.1*10/vw[i][1]*vw[i][0]
                return maxV
            else:
                maxV += vw[i][0]
                capacity -= vw[i][1]
        return maxV

    def recur_create_preorder(self,  root):
        '''通过递归使用合适的节点创建树'''
        if root is None:
            return
        '''需要一系列计算来创造节点'''
        '''满足一定条件才创建左节点，不然返回'''
        capacity = root.capacity - self.w[root.index]
        if capacity >= 0:
            value = root.value + self.v[root.index]
            self.maxV = max(self.maxV, value)
            index = root.index + 1
            '''计算最优解'''
            op = value + self.get_max_value(capacity, self.w[index:], self.v[index:])
            if self.maxV <= op:
                root.l_child = Node(op, value, capacity, index)
                if self.maxV == op:
                    return
                '''根据index来计算最优值'''
                if root.l_child.index < self.deep_tree:
                    self.recur_create_preorder(root.l_child)

        '''满足一定条件才能创建右节点，不然返回'''
        capacity = root.capacity
        value = root.value
        index = root.index + 1
        '''计算最优解'''
        op = value + self.get_max_value(capacity, self.w[index:], self.v[index:])
        if self.maxV <= op:
            root.r_child = Node(op, value, capacity, index)
            if self.maxV == op:
                return
            if root.r_child.index < self.deep_tree:
                self.recur_create_preorder(root.r_child)

    def recur_preorder_trvalsal(self, root):
        '''递归实现先序遍历'''
        if root is None:
            return
        print root.value
        self.recur_preorder_trvalsal(root.l_child)
        self.recur_preorder_trvalsal(root.r_child)


def test():
    v = [5, 6, 3, 1]
    w = [4, 5, 2, 1]
    capacity = 9
    root = Node(0, 0, capacity)
    tree = Optimal_dps_tree(root, capacity, w, v)
    tree.recur_create_preorder(tree.root)
    tree.recur_preorder_trvalsal(tree.root)


if __name__ == '__main__':
    test()
