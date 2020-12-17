n, k = map(int, input().split())

count = 0
while 1:
    if n < k:
        count = count + n - 1
        break
    n = n / k
    count += 1

print(int(count))
