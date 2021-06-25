#uniquestring
import math
le=pow(10,9)+7
def pos(n):
	p=0
	for x in range(1,(n//2)+1):
		y=n-x
		p+=math.factorial(y)/math.factorial(x)*math.factorial(y-x)
	return int(p)				

s=input()
if 'c' in s or 'k' in s:
	print('0')
else:
	i,c,c1=0,0,0
	l=[]
	for i in range(len(s)):
		if s[i]=='f':
			c+=1
		elif c>1:
			l.append(c)
			c=0
		if s[i]=='g':
			c1+=1
		elif c1>1:
			l.append(c1)
			c1=0
	if c>1:
		l.append(c)
	if c1>1:
		l.append(c1)
	c=len(l)
	l.sort()
	l1=[i for i in l if i>2]
	c1=len(l1)
	k=int((1<<c)/(1<<c1))
	if c==0:
		print('1')
	elif c1==0:
		print(k)
	else:
		s1=0
		for i in range(1,1<<len(l1)):
			s=1
			for j in range(31):
				if i>>j&1:
					a=pos(l1[c1-j-1])
					s=s*a
			s1=s1+(s*k)
		print((s1+k)%le)
	
	
	

