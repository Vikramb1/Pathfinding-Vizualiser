from queue import PriorityQueue

def dfs(start, end, maze):
    stack = []
    stack.append(start)
    visited = set()
    adjacent = [[1,0],[0,1],[-1,0],[0,-1]]
    parents = {}
    final = []
    while len(stack) > 0:
        curr = stack.pop()
        visited_copy = visited.copy()
        visited.add(curr)
        final.append(list(visited-visited_copy))
        for k in adjacent:
            x1 = curr[0] + k[0]
            y1 = curr[1] + k[1]
            visited_copy = set()
            visited1_copy = set()
            if 0 <= x1 < len(maze) and 0 <= y1 < len(maze[0]) and (x1,y1) not in visited and maze[x1][y1] != 1:
                if (x1,y1) == end:
                    parents[(x1,y1)] = curr
                    path = []
                    c = end
                    while c != start:
                        path.append(c)
                        c = parents[c]
                    return path, final
                else:
                    parents[(x1,y1)] = curr
                    stack.append((x1,y1))



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