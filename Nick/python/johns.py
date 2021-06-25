import math
def root(n,c):
	a=math.sqrt(n)
	if a-int(a)==0:
		c+=1
		root(a,c)
	else:
		print('0')
for w in range(int(input())):
	n=int(input())
	c=0
	ans=root(n,c)
	