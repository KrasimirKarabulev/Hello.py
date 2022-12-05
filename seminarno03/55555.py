number = int(input("Please insert a number: "))
k=1
total=0
for i in range(number):
    if i==number-1:
        print(number*k, end=" = ")
        total+=number*k
    else:
        print(number*k, end=" + ")
        total+=number*k
        k=(k*10)+1
print(total)
    
