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
    """l1 = []
    l3 = []
    z=[]
    k = problem.getStartState()
    l1.append(k)
    l4 = problem.getSuccessors(problem.getStartState())
    for item in l4:
        s.push(item)
    while s.isEmpty()==False and problem.isGoalState(k) != True:
        k1 = s.pop()
        k=k1[0]
        l3.append(k1[1])
        l1.append(k)
        if(problem.isGoalState(k) != True): 
            l2 = problem.getSuccessors(k1[0])
            i=0
            for item in l2:
                if(item[0] not in l1):
                    s.push(item)
                elif len(l2)>0 and item[0] in l1:
                    z.append(item)
            if len(z) == len(l2) or len(l2)==0:
                y=l3.pop()
            z=[]
    return l3"""
    s = util.Stack()
    visited = []
    z=[]
    s.push((problem.getStartState(),[]))
    k = problem.getStartState()
    while s.isEmpty()==False and problem.isGoalState(k) != True:
        k,act = s.pop()
        s.push((k,act))
        visited.append(k)
        if(problem.isGoalState(k) == False):
            l2 = problem.getSuccessors(k)
            for item in l2:
                if(item[0] not in visited):
                    s.push((item[0],act + [item[1]]))
                elif len(l2)>0 and item[0] in visited:
                    z.append(item)
            if len(z) == len(l2):
                y,r=s.pop()
            z=[]
    return act        

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    q = util.Queue()
    q.push((problem.getStartState(),[]))
    visited = []
    k = problem.getStartState()
    act = []
    while q.isEmpty()==False and problem.isGoalState(k) == False:
        k,act = q.pop()
        
        if(problem.isGoalState(k) == False and k not in visited):
            l2 = problem.getSuccessors(k)
            for item in l2:
                if(item[0] not in visited):
                    q.push((item[0],act + [item[1]]))
        visited.append(k)
    return act                
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    pq.push((problem.getStartState(),[]),0)
    co={}
    visited = []
    co[problem.getStartState()] = 0
    k = problem.getStartState()
    while pq.isEmpty()==False and problem.isGoalState(k) == False:
        k,act = pq.pop()
        if(problem.isGoalState(k) == False and k not in visited):
            l2 = problem.getSuccessors(k)
            for item in l2:
                if(item[0] not in visited):
                    pq.push((item[0],act + [item[1]]),co[k]+item[2])
                    co[item[0]] = co[k]+item[2]
        visited.append(k)
    return act   
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    pq.push((problem.getStartState(),[]),heuristic(problem.getStartState(),problem))
    co={}
    visited = []
    co[problem.getStartState()] = 0
    k = problem.getStartState()
    while pq.isEmpty()==False and problem.isGoalState(k) == False:
        k,act = pq.pop()
        if(problem.isGoalState(k) == False and k not in visited):
            l2 = problem.getSuccessors(k)
            for item in l2:
                if(item[0] not in visited):
                    pq.push((item[0],act + [item[1]]),co[k]+item[2]+heuristic(item[0],problem))
                    co[item[0]] = co[k]+item[2]
        visited.append(k)
    return act   
    util.raiseNotDefined()
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
