x,y=int(input()),int(input())
out=[]
for i in range(x):
    inter=[]
    for j in range(y):
        inter.append(i*j)
    out.insert(i,inter)
print(out)
    	