import numpy as np
from solution import astar,bfs,dfs,time

data = [0, 1, 2, 3, 4, 8, 6, 7, 5]
data1 = [0,1,2,3,4,5,6,7,8]
print(not(data == data1))
array = np.reshape(np.asarray(data), (-1,3))
print(array)
# print(array.flatten().tolist())
pos = np.where(array == 8)
row = pos[0].tolist()[0]
column = pos[1].tolist()[0]
print(type(row))
# print(t.generate_path(array))
# print(row[0],column[0])
# array[int(row[0])][int(column[0])] = 13
# print(array)
# class Node:
#     def __init__(self,data,add = None):
#         self.data = int(data)
#         self.add = add
# a = Node(4)
# b = Node(5)
# c = Node(6)
# print(a,b,c)
# a.add = b
# b.add = c
# if  5 in a:
#     print("hjsgf")
# else:
#     print("             fghjk")
# t = tree()
# print(t.possible_moves(current_puzzle=array))
# temp = t.possible_moves(array)
# for each in temp:
#     print(each)
# @time
def aprint():
    print("Decorator function")
a =[ 2, 1, 2, 1]
print(a)
print(min(a))
b = a.index(min(a))
print(b)
# print(astar([[0,8,2],[3,1,5],[6,4,7]]))
# astar([0, 1, 2, 3, 4, 5, 6, 8, 7])
# astar([0,5,6,4,2,1,3,7,8])
# bfs([0,5,6,4,2,1,3,7,8])
# bfs([0,8,2,4,1,5,3,6,7])
# bfs([0,2,5,4,1,7,3,6,8])
# bfs([0,2,5,4,1,7,8,3,6])
# astar([0,1,2,3,4,5,8,6,7])
# bfs([0,1,2,3,4,5,8,6,7])
# astar([0,1,8,3,4,2,6,7,5])
# bfs([0,1,8,3,4,2,6,7,5])
# astar([8,0,1,4,5,2,3,6,7])
# astar([0,8,2,4,1,5,3,6,7])
# astar([0,2,5,4,1,7,3,6,8])
# astar([0,2,5,4,1,7,8,3,6])
'''Puzzle - 1'''
astar([0,1,2,4,6,5,3,8,7])
bfs([0,1,2,4,6,5,3,8,7])

'''Puzzle - 2'''
astar([0,8,2,4,1,5,3,6,7])
bfs([0,8,2,4,1,5,3,6,7])

'''Puzzle - 3'''

astar([0,2,5,4,1,7,3,6,8])
bfs([0,2,5,4,1,7,3,6,8])