s="BANANA"
list1=[]
list2=[]
mylist=[]
for i in s:
	if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
		list1.append(i)
	else:
		list2.append(i)
list1=list(dict.fromkeys(list1))
list2=list(dict.fromkeys(list2))
mylist=list1+list2
print(mylist)
print(list1)
print(list2)