number =int(input("Въведи число: "))
array=[]
for i in range(number):
    array.append(int(input("Напълни масива: ")))
print(array)

while True:
    key=int(input("Веведи 0 или 1: "))
    if key==1:
        for i in range(len(array)):
            if i%2!=0:
                array[i]=array[i]+10  
        
                    
    elif key==0:
        for i in range(len(array)):
            if i%2==0:
                array[i]=array[i]+5
        
    elif key!=0 or key!=1:
        break
    print(array)
    
    


       
