for w in range(int(input())):
	n=int(input())
	c=0
	for i in range(1,n+1):
		for j in range(30):
			if (i>>j)&1 and (i>>j+1)&1:
				c+=1
				break
	print(c)