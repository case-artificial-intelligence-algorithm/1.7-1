#!/usr/bin/env python3

from my_solution import solution, StatusNode


# 测试用例
def test_solution():
    x1 = StatusNode(4, 40)  # 定义物品重量和价值，创建物品对象
    x2 = StatusNode(7, 42)
    x3 = StatusNode(5, 25)
    x4 = StatusNode(3, 12)
    root = StatusNode(0, 0) # 创建解空间树根节点
    item_list = [x1, x2, x3, x4]
    c = 10 # 背包容量

    # 正确答案
    correct_solution = 65
    
    # 程序求解结果
    result = solution(c, item_list, root)
    assert correct_solution == result

