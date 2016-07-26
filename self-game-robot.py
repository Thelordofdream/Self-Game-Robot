

class player:
    def __init__(self):
        self.Bullet = 0
        self.Vtimes = 0
        self.Rounds = 0
        self.History = []

player1 = player()
player2 = player()
player3 = player()
players = [player1, player2, player3]
each_round = [0, 0, 0]

while True:
    for i in range(3):
