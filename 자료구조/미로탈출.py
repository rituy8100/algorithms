from collections import deque

n,m=map(int,input().split())

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

queue=deque([])
movn=[1,0,-1,0]
movm=[0,1,0,-1]
queue.append([0,0])
while queue:
    v=queue.popleft()
    for i in range(4):
        if v[0]+movn[i]<0 or v[0]+movn[i]>=n or v[1]+movm[i]<0 or v[1]+movm[i]>=m:
            continue
        if array[v[0]+movn[i]][v[1]+movm[i]]==0:
            continue
        if array[v[0]+movn[i]][v[1]+movm[i]]==1:
            array[v[0] + movn[i]][v[1] + movm[i]]=array[v[0]][v[1]]+1
            queue.append([v[0] + movn[i],v[1] + movm[i]])

for i in range(n):
    print(array[i])

