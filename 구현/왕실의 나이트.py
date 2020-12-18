n=8
h=input()
x,y=ord(h[0]),int(h[1])
count=0
movx=[2,2,-2,-2,-1,1,-1,1]
movy=[-1,1,-1,1,2,2,-2,-2]

for i in range(8):
    nx=x+movx[i]
    ny=y+movy[i]
    if nx<ord('a') or nx>ord('h') or ny<1 or ny>8:
        continue
    count+=1
print(count)