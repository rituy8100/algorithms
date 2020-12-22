def dfs(graph, v, visited):
    visited[v] = True  # 방문처리
    print(v, end=' ')  # 방문노드 출력
    for i in graph[v]:  # 노드 v에 인접한 노드에
        if not visited[i]:  # 방문하지 않은 노드가 있으면
            dfs(graph, i, visited)  # 탐색한다


# 인접리스트 그래프
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
