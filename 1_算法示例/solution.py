#!/usr/bin/env python3
# 分治界限法解决0/1背包问题。

import collections

# 物品对象
class StatusNode:
    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value

def solution(c, item_list, Root):
    
    # 广度优先搜索分支限界算法
    def b_boundary1(c, item_list, Root):
        res, item_point = 0, 0 # res: 最大价值，item_point: 当前物品索引
        que = collections.deque()   # 创建队列
        que.append(Root)    # 将根节点放入队列
        while que and item_point < len(item_list):
            size = len(que)
            for _ in range(size):
                curnode = que.popleft() # 取出队列中的第一个节点
                current_weight = curnode.weight # 当前节点的重量
                current_value = curnode.value   # 当前节点的价值
                res = max(res, current_value)   # 更新最大价值
                new_weight1 = current_weight + item_list[item_point].weight # 装入新物品的重量
                new_value1 = current_value + item_list[item_point].value    # 装入新物品的价值

                # 装入新物品
                if new_weight1 <= c: # 装入新物品的重量不超过背包容量
                    new_node1 = StatusNode(new_weight1, new_value1) # 创建解节点
                    res = max(res, new_node1.value) # 更新最大价值
                    que.append(new_node1)   # 将解节点放入队列

                # 不装入新物品
                new_node2 = StatusNode(current_weight, current_value)   # 创建解节点
                que.append(new_node2)   # 将解节点放入队列
            item_point += 1 # 物品索引加1
        return res

    return b_boundary1(c, item_list, Root)



if __name__ == '__main__':
    x1 = StatusNode(4, 40)  # 定义物品重量和价值，创建物品对象
    x2 = StatusNode(7, 42)
    x3 = StatusNode(5, 25)
    x4 = StatusNode(3, 12)
    root = StatusNode(0, 0) # 创建解空间树根节点
    item_list = [x1, x2, x3, x4]
    c = 10 # 背包容量
    best_result = solution(c, item_list, root)
    print(f'装入背包物品所获得最大价值: {best_result}')

