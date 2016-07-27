from trees import *

mytree = grabTree('Tree.txt')
history = [0, -1, 0]
rate =float(predict(history, mytree, 2, 1))
print rate