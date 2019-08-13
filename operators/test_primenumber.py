primeFlag=True
y=1
i=int(input("Enter a integer number"))
#print(type(i))
#if i % 2 == 0: 
#    primeFlag=False
    
while y<i-1:
    y+=1
    print(y)
    if i % y == 0:
        print("divided by",y)
        primeFlag=False
    
if(primeFlag):
    print("Is a Prime Number")
else:
    print("Not a Prime Number")
    