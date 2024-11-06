n, m, v = map(int, input().split())
table = {i:[] for i in range(1, n + 1)}
visited = [False for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    table[x].append(y)
    table[y].append(x)


def dfs(node):
    if not visited[node-1]:
        visited[node-1] = True
        print(node, end=' ')
        for node in table[node]:
            dfs(node)

dfs(v)