# coding=utf-8
import random
import numpy as np

# 吸 = 积累一颗子弹 0
# Biu = 一级伤害,消耗一颗子弹 1
# 挡 = 能阻挡一级伤害,无消耗 -1
# BiuBiu = 二级伤害,消耗两颗子弹 2
# 挡挡 = 能阻挡一级和二级伤害,消耗一颗子弹 -2

class player:
    def __init__(self):
        self.Bullet = 0
        self.Vtimes = 0
        self.Rounds = 0
        self.History = []
        self.status = 1

moves = ["挡挡", "挡", "吸", "Biu", "BiuBiu"]
player1 = player()
player2 = player()
player3 = player()
players = [player1, player2, player3]
each_round = [0, 0, 0]
iteration = 0
num = 10
round_history = [[0] * 31 for i in range(3 * num)]

while iteration < num:
    print "*** Iteration %d ***" % (iteration + 1)
    count = 0
    losers = 0
    result = [0, 0, 0]
    while True:
        print "*** Round %d ***" % (count + 1)
        Max = -2
        # 出招
        for i in range(3):
            if players[i].Bullet == 0:
                each_round[i] = random.randint(-1, 0)
            elif players[i].Bullet == 1:
                each_round[i] = random.randint(-2, 1)
            elif players[i].Bullet >= 2:
                each_round[i] = random.randint(-2, 2)
            round_history[i + iteration * 3][count] = each_round[i]
            if players[i].status == 1 and each_round[i] >= Max:
                Max = each_round[i]
            # if players[i].status == 1:
            print "Player %d: %s" % ((i + 1), moves[each_round[i]+2])
        # 结算子弹
        for i in range(3):
            if players[i].status == 1:
                if each_round[i] == 0:
                    players[i].Bullet += 1
                elif each_round[i] == 1 or each_round[i] == -2:
                    players[i].Bullet -= 1
                elif each_round[i] == 2:
                    players[i].Bullet -= 2
                print "Player %d's bullet: %d" % ((i + 1), players[i].Bullet)
        # 结算结果
        for i in range(3):
            if players[i].status == 1:
                if (each_round[i] + Max) > 0 and each_round[i] != Max:
                    print "Player %d loss" % (i + 1)
                    players[i].status = 0
                    losers += 1
        if losers == 2:
            for i in range(3):
                if players[i].status == 1:
                    print "Player %d win" % (i + 1)
                    result[i] = 1
                    print result
                round_history[i+ iteration * 3][-1] = str(result[i])
            break
        count += 1
    for i in range(3):
        players[i].Bullet = 0
        players[i].status = 1
    iteration += 1
print np.array(round_history)