# coding=utf-8
from trees import *

# 吸 = 积累一颗子弹 0
# Biu = 一级伤害,消耗一颗子弹 1
# 挡 = 能阻挡一级伤害,无消耗 -1
# BiuBiu = 二级伤害,消耗两颗子弹 2
# 挡挡 = 能阻挡一级和二级伤害,消耗一颗子弹 -2

mytree = grabTree('Tree.txt')
history = [0, -1, 1, 0, -1, 0]
round = 1
move = 0
rate = float(predict(history, mytree, round - 1, move))
print round, move, rate

round = 2
move = -1
rate = float(predict(history, mytree, round - 1, move))
print round, move, rate

round = 3
move = 1
rate = float(predict(history, mytree, round - 1, move))
print round, move, rate

round = 4
move = 0
rate = float(predict(history, mytree, round - 1, move))
print round, move, rate

round = 5
move = -1
rate = float(predict(history, mytree, round - 1, move))
print round, move, rate

round = 6
move = 0
rate = float(predict(history, mytree, round - 1, move))
print round, move, rate

round = 7
move = 2
rate = float(predict(history, mytree, round - 1, move))
print round, move, rate
