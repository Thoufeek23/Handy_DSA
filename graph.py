from collections import deque

graph = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]

rows, cols = len(graph), len(graph[0])
directions = [[1,0], [-1,0], [0,1], [0,-1]]

def bfs(r, c):
    seen = set()
    ret = []
    q = deque()
    q.append((r, c))
    seen.add((r, c))
    while q:
        cr, cc = q.popleft()
        ret.append(graph[cr][cc])
        for dr, dc in directions:
            nr, nc = cr+dr, cc+dc
            if nr in range(rows) and nc in range(cols) and (nr, nc) not in seen:
                q.append((nr, nc))
                seen.add((nr, nc))
    return ret

def dfs(r, c):
    ret = []
    seen = set()
    stack = []
    stack.append((r, c))
    seen.add((r, c))
    while stack:
        cr, cc = stack.pop()
        ret.append(graph[cr][cc])
        for dr, dc in directions:
            nr, nc = cr+dr, cc+dc
            if nr in range(rows) and nc in range(cols) and (nr, nc) not in seen:
                stack.append((nr, nc))
                seen.add((nr, nc))
    return ret

ans_bfs = bfs(0, 0)
ans_dfs = dfs(0, 0)

print("BFS: ", ans_bfs)
print("DFS: ", ans_dfs)