N, K, M = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
count = 0
add = 0
while 1:
    for i in range(M):
        count += 1
        if count >= K:
            break
        add += data[0]
        print(add)
    if count >= K:
        break
    add += data[1]
    count += 1

print(add)
