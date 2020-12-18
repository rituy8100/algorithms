n = int(input())
arrays = list(input().split())
x, y = 1, 1
nx, ny = 0, 0
# L,R,U,D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
mov = ['L', 'R', 'U', 'D']

for array in arrays:
    for i in range(len(mov)):
        # 이동
        if array == mov[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 범위 벗어나면 스킵
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
        x, y = nx, ny

print(x, y)
