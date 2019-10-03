# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from pprint import pprint

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    print("start search")
    start = problem.getStartState()
    successors = problem.getSuccessors(start)
    # include position and direction
    arrived = set()
    path = []
    stack = []
    for suc in successors:
        stack.append(suc)
    pre = start
    parents_map = {}
    while stack:
        next = stack.pop()
        pos = next[0]
        dire = next[1]
        path.append(dire)
        if problem.isGoalState(pos):
            break
        successors = problem.getSuccessors(pos)
        for suc in successors:
            next_p = suc[0]
            next_d = suc[1]
            if next_p != pre and (next_p, next_d) not in arrived:
                parents_map[suc] = next
                stack.append(suc)
        pre = next[0]
        arrived.add((pos, dire))
    state_path = [next]
    for key, value in parents_map.items():
        assert key != value
    while True:
        p = parents_map.get(next, None)
        next = p
        if p:
            state_path.insert(0, p)
        else:
            break

    
    return [s[1] for s in state_path]

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    print("start search")
    start = problem.getStartState()
    successors = problem.getSuccessors(start)
    # include position and direction
    arrived = set()
    path = []
    queue = []
    for suc in successors:
        queue.append(suc)
    pre = start
    parents_map = {}
    while queue:
        next = queue.pop(0)
        pos = next[0]
        dire = next[1]
        path.append(dire)
        if problem.isGoalState(pos):
            break
        successors = problem.getSuccessors(pos)
        for suc in successors:
            next_p = suc[0]
            next_d = suc[1]
            if next_p != pre and next_p not in arrived:
                parents_map[suc] = next
                queue.append(suc)
        pre = next[0]
        arrived.add(pos)
        pprint(arrived)
    state_path = [next]
    for key, value in parents_map.items():
        assert key != value
    while True:
        p = parents_map.get(next, None)
        next = p
        if p:
            state_path.insert(0, p)
        else:
            break

    
    return [s[1] for s in state_path]

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    print("start search")
    start = problem.getStartState()
    successors = problem.getSuccessors(start)
    # include position and direction
    arrived = set()
    path = []
    queue = []
    for suc in successors:
        queue.append(suc)
    pre = start
    parents_map = {}
    while queue:
        # simplest, but not good
        queue = sorted(queue, key=lambda x: x[2])
        next = queue.pop(0)
        pos = next[0]
        dire = next[1]
        path.append(dire)
        if problem.isGoalState(pos):
            break
        successors = problem.getSuccessors(pos)
        # order by  cost
        for suc in successors:
            next_p = suc[0]
            next_d = suc[1]
            if next_p != pre and (next_p, next_d) not in arrived:
                parents_map[suc] = next
                queue.append(suc)
        pre = next[0]
        arrived.add((pos, dire))
    state_path = [next]
    for key, value in parents_map.items():
        assert key != value
    while True:
        p = parents_map.get(next, None)
        next = p
        if p:
            state_path.insert(0, p)
        else:
            break

    
    return [s[1] for s in state_path]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    print("start search")
    start = problem.getStartState()
    successors = problem.getSuccessors(start)
    # include position and direction
    arrived = set()
    path = []
    queue = []
    for suc in successors:
        queue.append(suc)
    pre = start
    parents_map = {}
    goal = problem.goal
    while queue:
        # simplest, but not good
        queue = sorted(queue, key=lambda x: x[2]+heuristic(x[0], problem))
        next = queue.pop(0)
        pos = next[0]
        dire = next[1]
        path.append(dire)
        if problem.isGoalState(pos):
            break
        successors = problem.getSuccessors(pos)
        # order by  cost
        for suc in successors:
            next_p = suc[0]
            next_d = suc[1]
            if next_p != pre and (next_p, next_d) not in arrived:
                parents_map[suc] = next
                queue.append(suc)
        pre = next[0]
        arrived.add((pos, dire))
    state_path = [next]
    for key, value in parents_map.items():
        assert key != value
    while True:
        p = parents_map.get(next, None)
        next = p
        if p:
            state_path.insert(0, p)
        else:
            break

    
    return [s[1] for s in state_path]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
