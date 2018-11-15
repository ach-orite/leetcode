import math,random

#网上找的打印树的一个函数，很好用，谁用谁知道
def print_tree(array): #打印堆排序使用
    '''
    深度 前空格 元素间空格
    1     7       0
    2     3       7
    3     1       3
    4     0       1
    '''
    # first=[0]
    # first.extend(array)
    # array=first
    index = 1
    depth = math.ceil(math.log2(len(array))) # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()

def sort(arr,start,end):
    if end == start * 2:
        if arr[start * 2] > arr[start]:
            arr[start * 2], arr[start] = arr[start], arr[start * 2]
    else:
        if end < start * 2 + 1:
            return
        else:
            left = arr[start*2]
            right = arr[start*2+1]
            if left>right and left > arr[start]:
                arr[start * 2 ], arr[start] = arr[start], arr[start * 2 ]
                sort(arr,start*2,end)
            if left<right and right > arr[start]:
                arr[start * 2+1], arr[start] = arr[start], arr[start * 2+1]
                sort(arr, start * 2+1, end)

def heapfiy(arr):
    x = len(arr) - 1
    n = x // 2
    while n > 0:
        # print(n)
        sort(arr, n, x)
        n -= 1

#以下是主函数

#第一个0是占位用
orignal_list=[0, 74, 73, 59, 72, 64, 69, 43, 36, 70, 61, 40, 16, 47, 67, 17, 31, 19, 24, 14, 20, 48, 5, 7, 3, 78, 84, 92, 97, 98, 99]
print(orignal_list)
#第一次构建最大堆
heapfiy(orignal_list)
#打印树
print_tree(orignal_list)

x= len(orignal_list) - 1
while x!=1:
    #交换最大的数和最后一个
    orignal_list[1],orignal_list[x]=orignal_list[x],orignal_list[1]
    x-=1
    #由于交换了，不再是最大堆，重新构建最大堆
    n=x//2
    while n>0:
        sort(orignal_list,n,x)
        n-=1

#打印最后结果
print_tree(orignal_list)
print(orignal_list)