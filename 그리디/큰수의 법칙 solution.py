n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count=int(m/(k+1))*k
count+=m%(k+1) #m이 k+1로 나누어지지 않을경우의 나머지를 더해줌

result=0
result += count*first
result += (m-count)*second

print(result)