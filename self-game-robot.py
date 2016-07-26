# coding=utf-8
import random

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

moves = ["挡挡", "挡", "吸", "Biu", "BiuBiu"]
player1 = player()
player2 = player()
player3 = player()
players = [player1, player2, player3]
each_round = [0, 0, 0]
count = 0

while count < 1:
    round_history1 = []
    round_history2 = []
    round_history3 = []
    round_history = [round_history1, round_history2, round_history3]
    for i in range(3):
        if players[i].Bullet == 0:
            each_round[i] = random.randint(-1, 0)
        elif players[i].Bullet == 1:
            each_round[i] = random.randint(-2, 1)
        elif players[i].Bullet >= 2:
            each_round[i] = random.randint(-2, 2)
        round_history[i].append(each_round[i])
    if i in range(3):
        if each_round[i] == 0:
            players[i].Bullet += 1
        elif each_round[i] == 1 or each_round[i] == -2:
            players[i].Bullet -= 1
        elif each_round[i] == 2:
            players[i].Bullet -= 2
        print
    for i in range(3):
        players[i].Bullet = 0
    count += 1