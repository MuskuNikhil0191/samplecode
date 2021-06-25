#socialdistance
import math
for t in range(int(input())):
	n,k=map(int,input().split())
	s=input()
	x=s.find('1')
	if x==-1:
		print(math.ceil(n/(k+1)))
	else:
		c=0
		i=x
		y=0
		while i!=-1:
			c+=math.floor((i-y)/(k+1))
			s=s[:i]+'0'+s[i+1:]
			y=i+1
			i=s.find('1')
		c+=math.floor((n-y)/(k+1))
		print(c)
				
			

			
