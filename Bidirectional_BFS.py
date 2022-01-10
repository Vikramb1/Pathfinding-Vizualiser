from queue import Queue

def bbfs(start, end, maze):
    visited = set()
    visited1 = set()
    adjacent = [[1,0],[0,1],[-1,0],[0,-1]]
    pq = Queue()
    pq1 = Queue()
    pq.put(start)
    pq1.put(end)
    parents = {}
    parents1 = {}
    final = []
    final1 = []
    while pq and pq1:
        (x,y) = pq.get()
        (a,b) = pq1.get()
        for k in adjacent:
            x1 = x+k[0]
            y1 = y+k[1]
            a1 = a+k[0]
            b1 = b+k[1]
            visited_copy = set()
            visited1_copy = set()
            if 0 <= x1 < len(maze) and 0 <= y1 < len(maze[0]) and (x1,y1) not in visited and maze[x1][y1] != 1:
                visited_copy = visited.copy()
                visited.add((x1,y1))
                pq.put((x1,y1))
                parents[(x1,y1)] = (x,y)
            if 0 <= a1 < len(maze) and 0 <= b1 < len(maze[0]) and (a1,b1) not in visited1 and maze[a1][b1] != 1:
                visited1_copy = visited1.copy()
                visited1.add((a1,b1))
                pq1.put((a1,b1))
                parents1[(a1,b1)] = (a,b)
            final.append(list(visited-visited_copy) + list(visited1-visited1_copy))
            if len(visited.intersection(visited1)) > 0:
                meeting = list(visited.intersection(visited1))[0]
                #parents[(x1,y1)] = (x,y)
                path = []
                curr = meeting
                h = [(start[0] + k[0],start[1] + k[1]) for k in adjacent]
                print(parents,curr)
                while curr != start:
                    #print(curr)
                    path.append(curr)
                    curr = parents[curr]
                parents1[(a1,b1)] = (a,b)
                curr1 = meeting
                w = [(end[0] + k[0],end[1] + k[1]) for k in adjacent]
                while curr1 not in w:
                    print(curr1)
                    path.append(curr1)
                    curr1 = parents1[curr1]
                path.append((0,0))
                return path, final



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
end = (7,7)
# result = bbfs(start,end,maze)
# path = result[0]
# result = result[1:][0]
# print(result)