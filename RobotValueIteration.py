# Calvin Aduma
# CPSC 4420
# Assignment 2

from turtle import position


class AssignmentTwo:
    def __init__(self):
        # { str: double }
        self.move_rewards = {
            # move1: move one cell forward. Cost: 1.5
            "A1" : -1.5,
            # move2: move two cells forward. Cost: 2
            "A2" : -2,
            # left: turn left. Cost 0.5
            "A3" : -0.5,
            # right turn right. Cost 0.5
            "A4" : -0.5
        }
        self.state_value = self.initializeStateValues()
        self.invalid_actions = [
            # (current_state, action)
            ((5,3,1),"A1"),((5,3,1),"A2"),((5,4,1),"A2"),((4,5,4),"A2"),
            ((5,2,1),"A2"),
            ((2,5,4),"A1"),((2,5,4),"A2"),
            ((1,5,4),"A2"),
            ((2,1,1),"A1"),((2,1,1),"A2"),
            ((3,1,1),"A1"),((3,1,1),"A2"),
            ((1,2,4),"A1"),((1,2,4),"A2"),
            ((1,3,4),"A1"),((1,3,4),"A2"),
            ((2,4,2),"A1"),((2,4,2),"A2"),((2,5,2),"A2"),
            ((3,3,3),"A1"),((3,3,3),"A2"),((3,3,2),"A1"),((3,3,2),"A2"),((3,4,2),"A2"),
            ((4,2,3),"A1"),((4,2,3),"A2"),((4,3,3),"A2"),((5,2,3),"A2"),
            ((1,1,3),"A1"),((1,2,3),"A1"),((1,3,3),"A1"),((1,4,3),"A1"),((1,5,3),"A1"),
            ((1,1,3),"A2"),((1,2,3),"A2"),((1,3,3),"A2"),((1,4,3),"A2"),((1,5,3),"A2"),
            ((2,1,3),"A2"),((2,4,3),"A2"),((2,5,3),"A2"),
            ((1,5,1),"A1"),((2,5,1),"A1"),((3,5,1),"A1"),((4,5,1),"A1"),
            ((1,5,1),"A2"),((2,5,1),"A2"),((3,5,1),"A2"),((4,5,1),"A2"),
            ((1,4,1),"A2"),((2,4,1),"A2"),((3,4,1),"A2"),((4,4,1),"A2"),((4,4,1),"A2"),
            ((5,1,4),"A1"),((5,2,4),"A1"),((5,3,4),"A1"),((5,4,4),"A1"),
            ((5,1,4),"A2"),((5,2,4),"A2"),((5,3,4),"A2"),((5,4,4),"A2"),
            ((4,1,4),"A2"),((4,2,4),"A2"),((4,3,4),"A2"),((4,4,4),"A2"),((4,5,4),"A2"),
            ((1,1,2),"A1"),((2,1,2),"A1"),((3,1,2),"A1"),((4,1,2),"A1"),((5,1,2),"A1"),
            ((1,1,2),"A2"),((2,1,2),"A2"),((3,1,2),"A2"),((4,1,2),"A2"),((5,1,2),"A2"),
            ((1,2,2),"A2"),((2,2,2),"A2"),((3,2,2),"A2"),((4,2,2),"A2"),((5,2,2),"A2"),
        ]
        self.blocks = [
            (2,2),(2,3),(3,2)
        ]
        self.current_state = (1, 1, 1)  
        self.gamma = 1
        self.goal = [(5, 5)]
        self.game_over = [(4, 4)]
        self.H = 100

    Dictionary = {tuple:int}
    # (i,j,direction) : Cost(int)
    def initializeStateValues(self)->Dictionary:
        temp_state_cost = {}
        for x in range(1,6):
            for y in range(1,6):
                for k in range(1,5):
                    if y == 2 and (x == 2 or x == 3):
                        temp_state_cost[(x, y, k)] = False
                        continue
                    if y == 3 and x == 2:
                        temp_state_cost[(x, y, k)] = False
                        continue
                    if x == 4 and y == 4:
                        temp_state_cost[(x, y, k)] = -1000
                        continue
                    if x == 5 and y == 5:
                        temp_state_cost[(x, y, k)] = 100
                        continue
                    temp_state_cost[(x, y, k)] = 0
        return temp_state_cost

    def doAction(self, state, action):
        direction = state[2]
        next_state = []
        if action == "A1":
            if self.isValidMove((state,action)):
                if direction == 1:
                    next_state = (state[0],state[1]+1,direction)
                elif direction == 2:
                    next_state = (state[0],state[1]-1,direction)
                elif direction == 3:
                    next_state = (state[0]-1,state[1],direction)
                elif direction == 4:
                    next_state = (state[0]+1,state[1],direction)
            else:
                return False
        elif action == "A2":
            if self.isValidMove((state,action)):
                if direction == 1:
                    next_state = (state[0],state[1]+2,direction)
                elif direction == 2:
                    next_state = (state[0],state[1]-2,direction)
                elif direction == 3:
                    next_state = (state[0]-2,state[1],direction)
                elif direction == 4:
                    next_state = (state[0]+2,state[1],direction)
            else:
                return False
        elif action == "A3":
            if self.isValidMove((state,action)):
                if direction == 1:
                    next_state = (state[0],state[1],3)
                elif direction == 2:
                    next_state = (state[0],state[1],4)
                elif direction == 3:
                    next_state = (state[0],state[1],2)
                elif direction == 4:
                    next_state = (state[0],state[1],1)
            else:
                return False
        elif action == "A4":
            if self.isValidMove((state,action)):
                if direction == 1:
                    next_state = (state[0],state[1],4)
                elif direction == 2:
                    next_state = (state[0],state[1],3)
                elif direction == 3:
                    next_state = (state[0],state[1],1)
                elif direction == 4:
                    next_state = (state[0],state[1],2)
            else:
                return False

        # print(state,action,next_state)
        return next_state

    def isValidMove(self, action_state):
        return True if action_state not in self.invalid_actions else False

    def ValueIterationAlgo(self):
        for iteration_number in range(1,self.H+1):
            if iteration_number <= 10:
                print("iter {}:".format(iteration_number))
            # loop for each row
            for i in range(1,6):
                # loop for each column
                for j in range(1,6):
                    # check if state is a win or game over
                    if (i,j) in self.game_over or (i,j) in self.goal or (i,j) in self.blocks:
                        continue
                    # loop for each position
                    for k in range(1,5):
                        Q = {}
                        state = (i, j, k)
                        # loop for each reward and action per state
                        for action, reward in self.move_rewards.items():
                            next_state = self.doAction(state,action)
                            if next_state is False:
                                continue
                            Q[action] = []
                            Q[action].append(reward + self.state_value[next_state])
                        # sets the max value of Q for each state
                        best_action = max(Q, key=Q.get)
                        self.state_value[(i,j,k)] = Q[best_action][0]
                        if iteration_number <= 10:
                            print("state ({},{},{}) V = {:.2f}\tBest Action: {}".format(i,j,k,self.state_value[(i,j,k)],best_action))
                
    def ValueIterationGammaAlgo(self):
        for iteration_number in range(1,self.H+1):
            # if iteration_number == 100:
            #     print("iter {}:".format(iteration_number))
            # loop for each row
            for i in range(1,6):
                # loop for each column
                for j in range(1,6):
                    # check if state is a win or game over
                    if (i,j) in self.game_over or (i,j) in self.goal or (i,j) in self.blocks:
                        continue
                    # loop for each position
                    for k in range(1,5):
                        Q = {}
                        state = (i, j, k)
                        # loop for each reward and action per state
                        for action, reward in self.move_rewards.items():
                            next_state = self.doAction(state,action)
                            if next_state is False:
                                continue
                            Q[action] = []
                            Q[action].append(reward + (self.gamma * self.state_value[next_state]))
                        # sets the max value of Q for each state
                        best_action = max(Q, key=Q.get)
                        self.state_value[(i,j,k)] = Q[best_action][0]
                        # if iteration_number == 100:
                        #     print("state ({},{},{}) V = {:.2f}\tBest Action: {}".format(i,j,k,self.state_value[(i,j,k)],best_action))

    def setH(self, H):
        self.H = H

    def setGamma(self, gamma):
        self.gamma = gamma

    def printStateValues(self):
        for i in range(1,6):
            for j in range(1,6):
                for k in range(1,5):
                    if self.state_value[(i,j,k)] is not False:
                        print("({},{},{}): {}".format(i,j,k,self.state_value[(i,j,k)]))

Board1 = AssignmentTwo()
Board2 = AssignmentTwo()
Board3 = AssignmentTwo()
# Question A
print("Question A: If there is no living reward/penalty, no onise, and no discount (gamma = 1),\nuse your common sense to find the best possible route from (1,1) to (5,5).\n")
print("Answer A: Best route is (1,1,4),(3,1,4),(4,1,4),(4,1,1),(4,3,1),(4,5,1),(4,5,4),(5,5,1)\n")

# Question B
print("Question B:")
print("Value Iteration Algorithm with 100 iterations. Results for first 10 iterations:")
Board1.ValueIterationAlgo()

# Question C
print("\nQuestion C:")
print("Answer C: It follows the same path, however the algorithm decided the best first action was A1 vs I decided the best was A2.")

# Question D
print("\nQuestion D:")
Board2.setGamma(0.8)
print("Answer D: The results match at the 10th iteration for Part B and Part D")
Board2.ValueIterationGammaAlgo()

# Question E
print("\nQuestion E:")
Board3.setGamma(0.2)
print("Answer E: The results do not match Part B or Part D at all. The agent never leaves the cell they start in unless it is at most 2 states away from the goal state. ")
Board3.ValueIterationGammaAlgo()
