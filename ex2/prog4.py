list=[]
x=int(input("Enter number: "))
for i in range(1,x+1):
    if x%i==0:
        list.append(i)
print(list)
