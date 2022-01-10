import random

def prims():
    grid = [[1 for r in range(40)] for i in range(40)]
    grid[0][0] = 0
    frontiers = getFontiers(grid,0,0,'blocked')
    while len(frontiers) > 0:
        curr = frontiers[-1]
        grid[curr[0]][curr[1]] = 0
        neighbours = getFontiers(grid,curr[0],curr[1],'passage')
        chosen = random.choice(neighbours)
        if chosen[0] == curr[0]:
            grid[chosen[0]][(chosen[1]+curr[1])//2] = 0
        else:
            grid[(chosen[0]+curr[0])//2][chosen[1]] = 0
        curr_frontier = getFontiers(grid,curr[0],curr[1],'blocked')
        frontiers = frontiers + curr_frontier
        frontiers.remove(curr)
    final = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                final.append((i,j))
    for k in range(40):
        final.append((0,k))
        final.append((k,0))
    return final

def getFontiers(grid,x,y,state):
    vals = []
    adjacent = [[2,0],[0,2],[-2,0],[0,-2]]
    for k in adjacent:
        x1,y1 = x+k[0],y+k[1]
        if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]):
            if grid[x1][y1] == 1:
                if state == 'blocked':
                    vals.append((x1,y1))
            elif state == 'passage':
                vals.append((x1,y1))
    return vals

k = prims()
# for t in k:
#     temp = []
#     for g in t:
#         if g == 1:
#             temp.append('#')
#         else:
#             temp.append('.')
