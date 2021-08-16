def ge(r):
  m=min(r)
  c=''
  for a in r:
    c+=str(a-m)
  return c
d=[[],['0000'],['00'],['10','001'],['01','100'],['01','10','101','000'],['00','20','000','011'],['02','00','000','110']]
C,P=map(int,input().split())
l=list(map(int,input().split()))
n=[0]*8
n[1]+=C
for k in range(2, 5):
  for i in range(C-k+1):
    for j in range(1, 8):
      if ge(l[i:i+k]) in d[j]:
        n[j]+=1
print(n[P])