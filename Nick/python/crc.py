def division(d,k):
    a=d[:len(k)]
    i=len(k)
    q=""
    p=a[0]
    q+=p
    if p=='0':
        b='0'*len(k)
    else:
        b=k
    while i<=len(d):
        x=xor(a,b)
        x=x[1:]
        if i==len(d):
            break
        a=x+d[i]
        p=a[0]
        q+=p
        if p=='0':
            b='0'*len(k)
        else:
            b=k
        i+=1
    return x
def xor(a,k):
    x=""
    for i in range(len(k)):
        if a[i]==k[i]:
            x+='0'
        else:
            x+='1'
    return x
data=input("enter the message:")
key=input("\nenter the key or divisor:")
print("\nSender's side:")
print("\noriginal message:",data)
app='0'*(len(key)-1)
newdata=data+app
print("\nbits to be appended:",app)
print("\nmessage after appending:",newdata)
rem=division(newdata,key)
print("\nremainder or checkvalue:",rem)
sent=data+rem
print("\nthe data sent or codeword:",sent)
print("\nReciever's side:")
print("\nthe data recieved:",sent)
rem=division(sent,key)
print("\nremainder or syndrome:",rem)
if int(rem)==0:
    print("\nSince the remainder is zero,there is no error")
else:
    print("\nerror detected")