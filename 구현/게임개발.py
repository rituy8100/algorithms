n,m=map(int,input().split())
x,y,z=map(int,input().split())
maps=[]
for i in range(n):
    maps.append(list(map(int, input().split())))

for i in range(n):
    print(maps[i])
maps[x][y]=1
movx=[-1,0,1,0]
movy=[0,-1,0,1]
dir=[0,1,2,3]
for j in range(4):
    for i in range(4):
        nz=(z+i)%4
        nx=x+movx[nz]
        ny=y+movy[nz]
        if maps[nx][ny]==1:
            continue
        x,y,z=nx,ny,nz
        maps[x][y]=1
        for k in range(n):
            print(maps[k])
        print('next')
        break

