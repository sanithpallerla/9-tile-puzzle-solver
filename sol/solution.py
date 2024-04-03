# Author : Sanith Kumar Pallerla
#This is the only file you need to work on. You do NOT need to modify other files

# Below are the functions you need to implement. For the first project, you only need to finish implementing bfs() and dfs()
import numpy as np
import copy
import datetime

global parent_node

class astar_Node:
    def __init__(self,data,g = 0,h = 0,parent = None, left = None, right = None, up = None, down = None):
        self.data = data
        self.g = g
        self.h = h
        self.parent = parent
        self.left = left
        self.right = right
        self.up = up
        self.down = down

def time(func):

    '''This is a decorator function used to calculate time of each search algorithm'''

    def wrapper(*args,**kwargs):

        start = datetime.datetime.now()
        print("Search started at",start)
        solution_node = func(*args,**kwargs)
        end = datetime.datetime.now()
        print("Search ended at",end)
        micro_sec = (end - start).total_seconds() * 1000000
        print("Time for execution of",func.__name__,"is", micro_sec,'microseconds')
        return solution_node
    return wrapper

def list_to_numpy(lst):
    '''This function is used to convert list into numpy array'''
    return np.reshape(np.asarray(lst), (-1,3))

class Node:
    def __init__(self,data,parent = None, left = None, right = None, up = None, down = None):
        self.data = np.reshape(np.asarray(data), (-1,3))
        self.parent = parent
        self.left = left
        self.right = right
        self.up = up
        self.down = down

class Tree:

    global parent_node

    def in_tree_search(self,parent_node,move):
        '''This function is used to find whether the passed move exists in their parent line or not'''
        queue = []
        queue.append(parent_node)
        while queue:
            # print("queue : ", queue)
            node = queue.pop(0)
            # print("In tree search : ", node.data)
            if move.tolist() == node.data.tolist():
                return 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node.up is not None:
                queue.append(node.up)
            if node.down is not None:
                queue.append(node.down)
        return 0
    def display(self):
        queue = []
        queue.append(parent_node)
        while queue:
            # print("queue : ", queue)
            node = queue.pop(0)
            # if move.data == node.data:
            #     return 0
            # print(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return 1


    def generate_tree(self,passed_node):
        '''This function is used to insert nodes into the tree according to direction of space moved'''
        parent_node = passed_node
        solution = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        queue = []
        queue.append(parent_node)
        while queue:
            node = queue.pop(0)
            changed_states = self.possible_moves(node)
            in_tree_status = [0,0,0,0]
            if changed_states[0] is not 0:
                in_tree_status[0] = self.in_tree_search(parent_node,changed_states[0])
            if changed_states[1] is not 0:
                in_tree_status[1] = self.in_tree_search(parent_node,changed_states[1])
            if changed_states[2] is not 0:
                in_tree_status[2] = self.in_tree_search(parent_node,changed_states[2])
            if changed_states[3] is not 0:
                in_tree_status[3] = self.in_tree_search(parent_node,changed_states[3])
            # if curent_state == node.data:
            if changed_states[0] is not 0 and not(in_tree_status[0]):
                node.left = Node(changed_states[0],node)
            if changed_states[1] is not 0 and not(in_tree_status[1]):
                node.right = Node(changed_states[1],node)
            if changed_states[2] is not 0 and not(in_tree_status[2]):
                node.up = Node(changed_states[2],node)
            if changed_states[3] is not 0 and not(in_tree_status[3]):
                node.down = Node(changed_states[3],node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node.up is not None:
                queue.append(node.up)
            if node.down is not None:
                queue.append(node.down)
            for each in changed_states:
                is_in_list = np.all(list_to_numpy(solution) == each)
                if is_in_list:
                    break
            # is_in_list = np.any(np.all(list_to_numpy(solution) == changed_states, axis=0))
            if is_in_list:
                if node.left is not None:
                    if solution == node.left.data.tolist():
                        return node.left
                if node.right is not None:
                    if solution == node.right.data.tolist():
                        return node.right
                if node.up is not None:
                    if solution == node.up.data.tolist():
                        return node.up
                if node.down is not None:
                    if solution == node.down.data.tolist():
                        return node.down
        return 0
    def possible_moves(self,current_puzzle):
        '''This function is used to generate all the possible moves from the current scenario'''
        pos = np.where(current_puzzle.data == 8)
        row = pos[0].tolist()[0]
        column = pos[1].tolist()[0]
        changed_states = [0,0,0,0]
        if row == 0:
            if column == 0:
                #Right Move : row-0, Column-0 to row-0, column-1
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[0][0], temp_puzzle[0][1] = temp_puzzle[0][1], temp_puzzle[0][0]
                changed_states[1] = copy.deepcopy(temp_puzzle)
                #Down Move : row-0, Column-0 to row-1, Column-0
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[0][0], temp_puzzle[1][0] = temp_puzzle[1][0], temp_puzzle[0][0]
                changed_states[3] = copy.deepcopy(temp_puzzle)
            if column == 1:
                #Left Move : row-0, Column-1 to row-0, Column-0
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[0][1],temp_puzzle[0][0] = temp_puzzle[0][0], temp_puzzle[0][1]
                changed_states[0] = copy.deepcopy(temp_puzzle)
                #Right Move : row-0, Column-1 to Row-0, Column -2
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[0][1], temp_puzzle[0][2] = temp_puzzle[0][2], temp_puzzle[0][1]
                changed_states[1] = copy.deepcopy(temp_puzzle)
                #Down Move : Row-0, Column-1 to Row-1, Column-1
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[0][1], temp_puzzle[1][1] = temp_puzzle[1][1], temp_puzzle[0][1]
                changed_states[3] = copy.deepcopy(temp_puzzle)
            if column == 2:
                #Left Move : Row-0, Column-2 to Row-0, Column-1
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[0][2],temp_puzzle[0][1] = temp_puzzle[0][1],temp_puzzle[0][2]
                changed_states[0] = copy.deepcopy(temp_puzzle)
                #Down Move : Row-0, Column-2 to Row-1, Column-2
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[0][2], temp_puzzle[1][2] = temp_puzzle[1][2], temp_puzzle[0][2]
                changed_states[3] = copy.deepcopy(temp_puzzle)
        elif row == 1:
            if column == 0:
                #Top Move : r1c0 to r0c0
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[1][0], temp_puzzle[0][0] = temp_puzzle[0][0], temp_puzzle[1][0]
                changed_states[2] = copy.deepcopy(temp_puzzle)
                #Right Move : r1c0 to r1c1
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[1][0], temp_puzzle[1][1] = temp_puzzle[1][1], temp_puzzle[1][0]
                changed_states[1] = copy.deepcopy(temp_puzzle)
                #Down Move : r1c0 to r2c0
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[1][0], temp_puzzle[2][0] = temp_puzzle[2][0], temp_puzzle[1][0]
                changed_states[3] = copy.deepcopy(temp_puzzle)
            if column == 1:
                #Left Move : r1c1 to r1c0
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[1][1], temp_puzzle[1][0] = temp_puzzle[1][0], temp_puzzle[1][1]
                changed_states[0] = copy.deepcopy(temp_puzzle)
                #Right move : r1c1 to r1c2
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[1][1], temp_puzzle[1][2] = temp_puzzle[1][2], temp_puzzle[1][1]
                changed_states[1] = copy.deepcopy(temp_puzzle)
                #Up Move : r1c1 to r0c1
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[1][1], temp_puzzle[0][1] = temp_puzzle[0][1], temp_puzzle[1][1]
                changed_states[2] = copy.deepcopy(temp_puzzle)
                #Down Move : r1c1 to r2c1
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[1][1], temp_puzzle[2][1] = temp_puzzle[2][1], temp_puzzle[1][1]
                changed_states[3] = copy.deepcopy(temp_puzzle)
                pass
            if column == 2:
                #Up Move : r1c2 to r0c2
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[1][2], temp_puzzle[0][2] = temp_puzzle[0][2], temp_puzzle[1][2]
                changed_states[2] = copy.deepcopy(temp_puzzle)
                #Left Move : r1c2 to r1c1
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[1][2], temp_puzzle[1][1] = temp_puzzle[1][1], temp_puzzle[1][2]
                changed_states[0] = copy.deepcopy(temp_puzzle)
                #Down Move : r1c2 to r2c2
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[1][2], temp_puzzle[2][2] = temp_puzzle[2][2], temp_puzzle[1][2]
                changed_states[3] = copy.deepcopy(temp_puzzle)
                pass
        elif row == 2:
            if column == 0:
                #Up Move : r2c0 to r1c0
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[2][0], temp_puzzle[1][0] = temp_puzzle[1][0], temp_puzzle[2][0]
                changed_states[2] = copy.deepcopy(temp_puzzle)
                #Right Move : r2c0 to r2c1
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[2][0], temp_puzzle[2][1] = temp_puzzle[2][1], temp_puzzle[2][0]
                changed_states[1] = copy.deepcopy(temp_puzzle)
                pass
            if column == 1:
                #Left Move : r2c1 to r2c0
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[2][1], temp_puzzle[2][0] = temp_puzzle[2][0], temp_puzzle[2][1]
                changed_states[0] = copy.deepcopy(temp_puzzle)
                #Up Move : r2c1 to r1c1
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[2][1], temp_puzzle[1][1] = temp_puzzle[1][1], temp_puzzle[2][1]
                changed_states[2] = copy.deepcopy(temp_puzzle)
                #Right Move : r2c1 to r2c2
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[2][1], temp_puzzle[2][2] = temp_puzzle[2][2], temp_puzzle[2][1]
                changed_states[1] = copy.deepcopy(temp_puzzle)
                pass
            if column == 2:
                #Left Move : r2c2 to r2c1
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[2][2], temp_puzzle[2][1] = temp_puzzle[2][1], temp_puzzle[2][2]
                changed_states[0] = copy.deepcopy(temp_puzzle)
                #Up Move : r2c2 to r1c2
                temp_puzzle = copy.deepcopy(current_puzzle.data)
                temp_puzzle[2][2], temp_puzzle[1][2] = temp_puzzle[1][2], temp_puzzle[2][2]
                changed_states[2] = copy.deepcopy(temp_puzzle)
                pass
        return changed_states

    def generate_path(self,node):
        '''This  Function is used to generate path travelled by space'''
        space_moved_data = []
        while node.parent is not None:
            space_moved_data.append(node.data.flatten().tolist())
            node = node.parent
        space_moved_data.append(node.data.flatten().tolist())
        path = []
        for each in space_moved_data:
            path.append(each.index(8))
        return path

    @time
    def bfs_search(self,node):
        '''This function is used to find the solution using bfs search'''
        solution = [[0,1,2],[3,4,5],[6,7,8]]
        queue = []
        queue.append(node)
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node.up is not None:
                queue.append(node.up)
            if node.down is not None:
                queue.append(node.down)
            if node.data.tolist() == solution:
                return node

    @time
    def dfs_search(self,node):
        '''This function is used to find the solution using DFS Search'''
        solution = [[0,1,2],[3,4,5],[6,7,8]]
        stack = []
        stack.append(node)
        while stack:
            node = stack.pop()
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            if node.up is not None:
                stack.append(node.up)
            if node.down is not None:
                stack.append(node.down)
            if node.data.tolist() == solution:
                return node

class astar_Tree(Tree):

    def bloodline_search(self,current_node,move):
        '''This function is used to find whether the current puzzle move exist in their line of existence'''
        node = current_node
        while node.parent is not None:
            try:
                if node.data.tolist() == move.tolist():
                    return 0
            except:
                print(node.parent,"\n",node.data)
            node = node.parent
        return 1

    @time
    def astar_search(self,node):
        '''This function is used to perform A* search'''
        solution = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        scores = []
        queue = []
        queue.append(node)
        cost_function = node.g + node.h
        scores.append(cost_function)
        index = 0
        while queue:
            min_score = min(scores)
            index = scores.index(min_score)
            scores.pop(index)
            # sorted(queue, key=lambda n: queue[n][])
            node = queue.pop(index)
            if node.data.tolist() == solution:
                return node
            if node.left is not None:
                cost_function = node.left.g + node.left.h
                queue.append(node.left)
                scores.append(cost_function)
            if node.right is not None:
                cost_function = node.right.g + node.right.h
                queue.append(node.right)
                scores.append(cost_function)
            if node.up is not None:
                cost_function = node.up.g + node.up.h
                queue.append(node.up)
                scores.append(cost_function)
            if node.down is not None:
                cost_function = node.down.g + node.down.h
                queue.append(node.down)
                scores.append(cost_function)

    def score(self,current_state):
        '''This function is used to calculate h cost of each node'''
        solution = list(range(9))
        current_state = current_state.flatten().tolist()
        score = 0
        for i in range(9):
            if current_state[i] != solution[i]:
                score += 1
        return score

    def generate_tree(self,parent_node):
        """This function is used generate tree with all possible moves of 8 puzzle"""
        solution = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        queue = []
        queue.append(parent_node)
        while queue:
            node = queue.pop(0)
            changed_states = self.possible_moves(node)
            if changed_states[0] is not 0 and self.bloodline_search(node,changed_states[0]):
                node.left = astar_Node(changed_states[0], (node.g+1), self.score(changed_states[0]),node)
            if changed_states[1] is not 0 and self.bloodline_search(node,changed_states[1]):
                node.right = astar_Node(changed_states[1], (node.g + 1), self.score(changed_states[1]), node)
            if changed_states[2] is not 0 and self.bloodline_search(node,changed_states[2]):
                node.up = astar_Node(changed_states[2], (node.g + 1), self.score(changed_states[2]), node)
            if changed_states[3] is not 0 and self.bloodline_search(node,changed_states[3]):
                node.down = astar_Node(changed_states[3], (node.g + 1), self.score(changed_states[3]), node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node.up is not None:
                queue.append(node.up)
            if node.down is not None:
                queue.append(node.down)

            for each in changed_states:
                is_in_list = np.all(list_to_numpy(solution) == each)
                if is_in_list:
                    break
            # is_in_list = np.any(np.all(list_to_numpy(solution) == changed_states, axis=0))
            if is_in_list:
                if node.left is not None:
                    if solution == node.left.data.flatten().tolist():
                        return node.left
                if node.right is not None:
                    if solution == node.right.data.flatten().tolist():
                        return node.right
                if node.up is not None:
                    if solution == node.up.data.flatten().tolist():
                        return node.up
                if node.down is not None:
                    if solution == node.down.data.flatten().tolist():
                        return node.down
        return 1

#here you need to implement the Breadth First Search Method = [0,8,2,3,1,4,6,7,5]
def bfs(puzzle):
    if puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return [8]
    parent_node = Node(list_to_numpy(puzzle))
    t= Tree()
    t.generate_tree(parent_node)
    solution_node = t.bfs_search(parent_node)
    path = t.generate_path(solution_node)
    path = path[:-1]
    path.reverse()
    return path

#here you need to implement the Depth First Search Method
def dfs(puzzle):
    if puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return [8]
    parent_node = Node(list_to_numpy(puzzle))
    t = Tree()
    t.generate_tree(parent_node)
    solution_node = t.dfs_search(parent_node)
    path = t.generate_path(solution_node)
    path = path[:-1]
    path.reverse()
    return path


#This will be for next project
def astar(puzzle):
    if puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return [8]
    parent_node = astar_Node(list_to_numpy(puzzle))
    t = astar_Tree()
    t.generate_tree(parent_node)
    solution_node = t.astar_search(parent_node)
    path = t.generate_path(solution_node)
    path = path[:-1]
    path.reverse()
    return path





