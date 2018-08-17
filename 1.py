def test(a,b):
	out=[]
	for i in range(a,b+1):
		if i%7==0 and i%5!=0:
			out.append(str(i))
		else:
			continue
	return out

print(','.join(test(200,300)))