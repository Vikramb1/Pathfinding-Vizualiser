from queue import PriorityQueue
from collections import defaultdict
from numpy import Inf

def djikstra(start, end, maze):
    adjacent = [[1,0],[0,1],[-1,0],[0,-1]]
    parents = {}
    costs = defaultdict(lambda: Inf)
    costs[start] = 0
    final = []
    pq = PriorityQueue()
    pq.put((0,start))
    visited = set()
    while pq:
        cost, (x,y) = pq.get()
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
            if 0 <= x1 < len(maze) and 0 <= y1 < len(maze[0]) and (x1,y1) not in visited and maze[x1][y1] != 1:
                new = costs[(x,y)] + 1
                if costs[(x1,y1)] > new:
                    parents[(x1,y1)] = (x,y)
                    costs[(x1,y1)] = new
                    pq.put((new,(x1,y1)))

    return parents

maze = [[0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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

start = (0,0)
end = (18,18)
# k = djikstra(start,end,maze)
