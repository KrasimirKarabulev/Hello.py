def input_nums(n):
    array=[]
    if not isinstance(n, int):
        return print(array)
    for i in range(n):
        i=input("Enter a list element: ")
        if i.isnumeric():
            array.append(int(i))
    return print(array)

def sum_list(lst):
    total=0
    isNumber=True
    for i in range(len(lst)):
        if type(lst[i])==int or type(lst[i])==float:
            total+=lst[i]
        elif type(lst[i])==str:
            for j in lst[i]:
                if (j <"0" or j>"9") and j!=".":
                    isNumber=False
                    break
                else:
                    isNumber=True
            if isNumber==True:
                total+=float(lst[i]) 
    return print(total)

def max_of_two(a,b):
    isANumber=True
    isBNumber=True
    if (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float):
        
        if a>b:
            return print(a)
        elif a<b:
            return print(b)
        elif a==b:
            return print(a)
    elif type(a)==str or type(b)==str:
        if type(a)==str and (type(b)==int or type(b)==float):

            for i in a:
                if (i<"0" or i>"9") and i!=".":
                    isANumber=False
                    break
                else: 
                    isANumber=True
        elif type(b)==str and (type(a)==int or type(a)==float):
            for i in b:
                if (i<"0" or i>"9") and i!=".":
                    isBNumber=False
                    break
                else: 
                    isBNumber=True
        else:
             return print("\n")
        if isANumber==True and isBNumber==True:
            a=float(a)
            b=float(b)
            if a>b:
                return print(a)
            elif a<b:
                return print(b)
            elif a==b:
                return print(a)
        elif isANumber==True and isBNumber==False:
            return print(a)
        elif isANumber==False and isBNumber==True:
            return print(b)
       

    
# n=input("Enter a number: ")
# if n.isnumeric():
#     input_nums(int(n))
# else:
#     input_nums(n) 

print("======================")

input_nums(3)

print("======================")

input_nums('a')

print("======================")

sum_list([1, "a", 3.14, "5"])

print("======================")

sum_list(["asd", "-"])

print("======================")

max_of_two(2.5, 13)

print("======================")

max_of_two("@#$", {})

print("======================")

max_of_two('a', 5)
