even=[]
x=int(input("Enter Number: "))
y=int(input("Enter Number: "))
if x<y:
    a=x;b=y
else:
    a=y;b=x
for i in range(a,b+1):
    if i%2==0:
        even.append(i)
print(even)