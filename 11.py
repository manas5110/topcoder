in_var=input().split(',')
out_var=[]
for x in in_var:
    l=len(x)
    val=0
    for i in range(l):
        val+=(2**i)*int(x[l-i-1])
    if val%5 == 0:
        out_var.append(x)
print(','.join(out_var))