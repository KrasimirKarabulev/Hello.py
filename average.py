def average(list, multiplier=1):
    count=0
    total=0
    isNumber=True
    if type(multiplier)!=int:
        return "Error"
    
    for i in range(len(list)):
        
        if type(list[i])==int or type(list[i])==float:
            total+=list[i]*multiplier
            count+=1
        elif type(list[i])==str:
            for j in list[i]:
                if (j <"0" or j>"9") and j!=".":
                    isNumber=False
                    break
                else:
                    isNumber=True
            if isNumber==True:
                total+=float(list[i])*multiplier
                count+=1   
            
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