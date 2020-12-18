n, m = map(int, input().split())
x, y, z = map(int, input().split())
maps = []
d = [[0] * m for _ in range(n)]
for i in range(n):
    maps.append(list(map(int, input().split())))

for i in range(n):
    print(maps[i])
print("시작!!")
d[x][y] = 1
movx = [-1, 0, 1, 0]
movy = [0, -1, 0, 1]
dir = [0, 1, 2, 3]
bool = 1
result = 1
while bool:
    count = 0
    for i in range(4):
        nz = (z + i) % 4
        nx = x + movx[nz]
        ny = y + movy[nz]
        count += 1
        if maps[nx][ny] == 1 or d[nx][ny] == 1:
            if count == 4:
                nx = x - movx[z]
                ny = y - movy[z]
                if d[nx][ny] == 1:
                    x, y = nx, ny
                    break
                else:
                    bool = 0
                    break
            continue
        x, y, z = nx, ny, nz
        d[x][y] = 1
        result += 1
        for k in range(n):
            print(d[k])
        print('next')

print(result)
