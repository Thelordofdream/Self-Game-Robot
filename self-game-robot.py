# coding=utf-8
import random
import numpy as np
from treePlotter import createPlot
from trees import *

# 吸 = 积累一颗子弹 0
# Biu = 一级伤害,消耗一颗子弹 1
# 挡 = 能阻挡一级伤害,无消耗 -1
# BiuBiu = 二级伤害,消耗两颗子弹 2
# 挡挡 = 能阻挡一级和二级伤害,消耗一颗子弹 -2


class player:
    def __init__(self):
        self.Bullet = 0
        self.History = []
        self.status = 1


def calculate(x):
    y = 2.41 * (x - 0) * (x - 0.17) - 7.08 * (x - 0) * (x - 1) + 2.94 * (x - 0.17) * (x - 1)
    return y


def self_random(y):
    y = [int(each*100) for each in y]
    m = len(y)
    s = sum(y)
    pos = 0
    rand = random.randint(0, s)
    for i in range(m):
        S = sum(y[:i])
        if rand > S:
            pos = i
    return pos

moves = ["挡挡", "挡", "吸", "Biu", "BiuBiu"]
people = 7
player1 = player()
player2 = player()
player3 = player()
player4 = player()
player5 = player()
player6 = player()
player7 = player()
players = [player1, player2, player3, player4, player5, player6, player7]
each_round = [0, 0, 0, 0, 0, 0, 0]
iteration = 0
num = 200
round_history = [[0] * 61 for i in range(people * num)]

while iteration < num:
    print "*** Iteration %d ***" % (iteration + 1)
    count = 0
    losers = 0
    result = [0, 0, 0, 0, 0, 0, 0]
    while True:
        print "*** Round %d ***" % (count + 1)
        Max = -2
        # 出招
        for i in range(people):
            predict_list = []
            if players[i].status == 1:
                if players[i].Bullet == 0:
                    move = [-1, 0]
                    y = [1, 1]
                    if iteration >= 1:
                        for want in range(-1, 1):
                            try:
                                 x = float(predict(round_history[i + iteration * people], mytree, count, want))
                                 y[want + 1] = calculate(x)
                            except:
                                pass
                    each_round[i] = move[self_random(y)]
                elif players[i].Bullet == 1:
                    move = [-2, -1, 0, 1]
                    y = [1, 1, 1, 1]
                    if iteration >= 1:
                        for want in range(-2, 2):
                            try:
                                 x = float(predict(round_history[i + iteration * people], mytree, count, want))
                                 y[want + 2] = calculate(x)
                            except:
                                pass
                    each_round[i] = move[self_random(y)]
                elif players[i].Bullet >= 2:
                    move = [-2, -1, 0, 1, 2]
                    y = [1, 1, 1, 1, 1]
                    if iteration >= 1:
                        for want in range(-2, 3):
                            try:
                                 x = float(predict(round_history[i + iteration * people], mytree, count, want))
                                 y[want + 2] = calculate(x)
                            except:
                                pass
                    each_round[i] = move[self_random(y)]
                round_history[i + iteration * people][count] = each_round[i]
                if each_round[i] >= Max:
                    Max = each_round[i]
                # if players[i].status == 1:
                print "Player %d: %s" % ((i + 1), moves[each_round[i] + 2])
        # 结算子弹
        for i in range(people):
            if players[i].status == 1:
                if each_round[i] == 0:
                    players[i].Bullet += 1
                elif each_round[i] == 1 or each_round[i] == -2:
                    players[i].Bullet -= 1
                elif each_round[i] == 2:
                    players[i].Bullet -= 2
                # print "Player %d's bullet: %d" % ((i + 1), players[i].Bullet)
        # 结算结果
        for i in range(people):
            if players[i].status == 1:
                if (each_round[i] + Max) > 0 and each_round[i] != Max:
                    print "Player %d lose" % (i + 1)
                    players[i].status = 0
                    losers += 1
        if losers == (people - 1):
            for i in range(people):
                # players[i].Rounds += 1
                if players[i].status == 1:
                    print "Player %d win" % (i + 1)
                    result[i] = 1
                    # players[i].Vtimes += 1
                round_history[i + iteration * people][-1] = str(result[i])
            break
        count += 1
    for i in range(people):
        players[i].Bullet = 0
        players[i].status = 1
    iteration += 1
    mytree = createTree(round_history[:7*iteration])

storeTree(mytree, "Tree.txt")
createPlot(mytree)
