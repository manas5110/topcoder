#Code starts here
in_vals=map(int,input().split(','))
C,H=50,30
out=[]
for D in in_vals:
    out.append((2*C*D)/H)
print(','.join(str(int(x)) for x in out))
