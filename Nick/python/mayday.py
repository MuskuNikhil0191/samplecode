n,q=map(int,input().split())
for w in range(q):
	t=[0]*31
	l,h,k=map(int,input().split())
	l1=bin(n)[2:]
	l1=l1[::-1]	
	for i in range(len(l1)):
		t[i]=int(l1[i])
	ans=0
	while(k>0):
		h1=t[h]
		for i in range(h,l,-1):
			t[i]=t[i-1]
		t[l]=h1
		k-=1
	for i in range(31):
		ans+=t[i]*(1<<i)
	print(ans)