from queue import Queue

def bfs(start, end, maze):
    visited = set()
    adjacent = [[1,0],[0,1],[-1,0],[0,-1]]
    pq = Queue()
    pq.put(start)
    parents = {}
    final = []
    while pq:
        (x,y) = pq.get()
        for k in adjacent:
            x1 = x+k[0]
            y1 = y+k[1]
            visited_copy = set()
            visited1_copy = set()
            if 0 <= x1 < len(maze) and 0 <= y1 < len(maze[0]) and (x1,y1) not in visited and maze[x1][y1] != 1:
                visited_copy = visited.copy()
                visited.add((x1,y1))
                final.append(list(visited-visited_copy))    
                if (x1,y1) == end:
                    parents[(x1,y1)] = (x,y)
                    path = []
                    curr = end
                    while curr != start:
                        path.append(curr)
                        curr = parents[curr]
                    return path, final
                else:
                    parents[(x1,y1)] = (x,y)
                    pq.put((x1,y1))



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
end = (3,3)
# result = bfs(start,end,maze)
# path = result[0]
# result = result[1:][0]
#print(result)