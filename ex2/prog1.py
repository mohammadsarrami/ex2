even=[]
x=int(input("Enter First Number : "))
y=int(input("Enter Second Number : "))
for i in range(x,y+1):
    if i%2==0:
        even.append(i)
print(even)