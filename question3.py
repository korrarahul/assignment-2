data=list(map(float,input("Nested Interactive Loop : ").split()))
a=[]
for i in data:
    i=i*2.54
    a.append(i)
print(a)

data2=list(map(float,input("List Comprehensation : ").split()))
b=[i*2.54 for i in data2]
print(b)