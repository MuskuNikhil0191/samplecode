#help nikhil
n,m=map(int,input().split())
s1=[]
s2=[]
for i in range(n+m):
	if i<n:
		s1.append(input())
	else:
		s2.append(input())
c=0
for i in s1:
	for j in s2:
		s=list(i+j)
		s=list(dict.fromkeys(s))
		if len(s)==26:
			c+=1
print(c)