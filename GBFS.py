from queue import PriorityQueue

def manhattan(x1,y1,end):
    return abs(x1-end[0]) + abs(y1-end[1])

def gbfs(start, end, maze):
    openlist = []
    openlist.append([0,start])
    closed = set()
    adjacent = [[1,0],[0,1],[-1,0],[0,-1]]
    parents = {}
    final = []
    while len(openlist) > 0:
        current = openlist.pop(0)
        closed_copy = closed.copy()
        closed.add(current[1])
        final.append(list(closed-closed_copy))
        for k in adjacent:
            x1 = current[1][0]+k[0]
            y1 = current[1][1]+k[1]
            visited_copy = set()
            visited1_copy = set()
            if 0 <= x1 < len(maze) and 0 <= y1 < len(maze[0]) and (x1,y1) not in closed and maze[x1][y1] != 1:
                if (x1,y1) == end:
                    parents[(x1,y1)] = current[1]
                    path = []
                    curr = end
                    while curr != start:
                        path.append(curr)
                        curr = parents[curr]
                    return path, final
                else:
                    openlist.append([manhattan(x1,y1,end),(x1,y1)])
                    parents[(x1,y1)] = current[1]
        openlist = sorted(openlist, key=lambda x: x[0])

        





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
#print(gbfs(start,end,maze))