n,m=map(int,input().split())

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))


def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if array[x][y]==0:
        array[x][y]=1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False


count=0
for j in range(n):
    for k in range(m):
        if dfs(j,k)==True:
            count+=1

print(count)