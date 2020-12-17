n, m = map(int, input().split())

min_value = 0
max_value = 0

for i in range(n):
    data = list(map(int, input().split())) # 한 행씩 입력받는다
    min_value = min(data) # 한 행에서 가장 작은값
    max_value = max(min_value, max_value) #작은값중에 가장 큰 값

print(max_value)
