from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # input: head of the graph (node, neighbors -> list of nodes)
        # fyi: undirected, connected
        # does this have a cycle? (possibly)
        # no duplicate edges and no self-loops
        # edge cases: null state, one node, two nodes central node (star node)
        # output: head of the cloned graph (deep copy)

        # keep track of visited nodes (mark visited once copied)
        # 1 -> [2] -> copy the current node (copy the value in a new node, copy the neighbors)
        # 2 -> [1,3]
        # 3 -> [2]

        # handle null edge case: 
        if not node:
            return None

        if not node.neighbors:
            return Node(node.val)

        # intiailze the set visited, queue with the head value, empty clone Node, clonequeue with the clone value
        # set clone val to curr val
        cloneHash, clone = {}, Node(node.val)
        q, cq = deque([node]), deque([clone])
        # conduct bfs
        # iterate until queue is emtpy
        while q:
            # pop element in queue and set it to variable curr
            curr = q.popleft()
            # pop element in cqueue and set it to clone
            cloneCurr = cq.popleft()

            # if not cloneHash (check  from the original graph node)
                # run a loop through curr neighbors
            for neighbor in curr.neighbors:
            #     # on our newNode copy each neighbors value with a newNode
                if neighbor in cloneHash:
                    nclone = cloneHash[neighbor]                    
                else:
                    nclone = Node(neighbor.val)
                    cloneHash[neighbor] = nclone
                    cq.append(nclone)
                    q.append(neighbor)
                
                cloneCurr.neighbors.append(nclone)
        
            cloneHash[curr] =  cloneCurr
            # print("clone", cloneCurr.val, cloneCurr.neighbors)        
            # print("original", curr.val, curr.neighbors)        

        return clone

        