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


class node():
    def __init__(self, op=0,  value=0, capacity=0):
        self.__optimal = op
        self.__value = value
        self.__capacity = capacity
        self.__index = []


def optimal_dps_tree(capacity, wNumbers, w, v):
    return 0


def test():
    v = [5, 6, 3, 1]
    w = [4, 5, 2, 1]
    k = 8
    j = 3
    result = optimal_iteration(k, j, w, v)
    print result


if __name__ == '__main__':
    test()
