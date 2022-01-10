from queue import PriorityQueue
from collections import defaultdict
from numpy import Inf
import time
import math

def manhattan(x1,y1,end):
    return math.sqrt(abs(x1-end[0])**2 + abs(y1-end[1])**2)

def astar(start, end, maze):
    final = []
    adjacent = [[1,0],[0,1],[-1,0],[0,-1]]
    parents = {}
    costs = defaultdict(lambda: [Inf,Inf])
    pcosts[start] = [0,manhattan(start[0],start[1],end)]
    pq = PriorityQueue()
    pq.put((manhattan(start[0],start[1],end),start))
    visited = set()
    while pq:
        cost, (x,y) = pq.get()
        if (x,y) in visited:
            continue
        visited_copy = visited.copy()
        visited.add((x,y))
        final.append(list(visited-visited_copy))
        if (x,y) == end:
            path = []
            curr = end
            while curr != start:
                path.append(curr)
                curr = parents[curr]
            return path, final
        for k in adjacent:
            x1 = x+k[0]
            y1 = y+k[1]
            visited_copy = set()
            visited1_copy = set()
            if 0 <= x1 < len(maze) and 0 <= y1 < len(maze[0]) and maze[x1][y1] != 1:
                temp = costs[(x1,y1)][0] + 1 + manhattan(x1,y1,end)
                if (x1,y1) in visited and temp > sum(costs[(x1,y1)]):
                    continue
                if temp <= sum(costs[(x1,y1)]) or (x1,y1) not in [i[1] for i in pq.queue]:
                    parents[(x1,y1)] = (x,y)
                    costs[(x1,y1)] = [costs[(x,y)][0]+1,manhattan(x1,y1,end)]
                    pq.put((sum(costs[(x1,y1)]),(x1,y1)))
                # pq.put((cost+1+manhattan(x1,y1,end),(x1,y1)))
                # costs[(x1,y1)] = [cost+1,manhattan(x1,y1,end)]
                # parents[(x1,y1)] = (x,y)

maze = [[0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

# start = (0,0)
# end = (10,10)
# result = astar(start,end,maze)
# path = result[0]
# #print(path)
# result = result[1:][0]