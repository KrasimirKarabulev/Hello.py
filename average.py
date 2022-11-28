import numbers
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
def average(list, multiplier=1):
    count=0
    total=0
    if type(multiplier)!=int:
        return "Error"
    
    for i in range(len(list)):
        if is_number(str(list[i])):
            
            count+=1
            total+=float(list[i])*multiplier
    if count==0:
        print("Error: Devision by 0")
        return 

    return total/count  
    
print(average(['4', 1.5, "@7$", 3.5, (1, "hi")]))

print("===================")

print(average(['6', 3, 3.0], 2))

print("===================")

print(average(['%$', {}]))

print("===================")

print(average([]))