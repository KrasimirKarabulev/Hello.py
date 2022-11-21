number=int(input("Въведи число: "))
number1=0
number2=1
total=0
for i in range(0,number+2):
    print(number1, end=" ")
    total=number1+number2
    number1=number2
    number2=total

    
