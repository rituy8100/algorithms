# 인접행렬
# 모든 정보저장하기때문에 메모리 비효율적 but 연결여부 확인 쉬움
INF = 99999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 인접리스트
# 연결된 노드정보만 저장하기 때문에 메모리 효율적 but 연결여부확인 오래걸림
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보(노드,거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)
