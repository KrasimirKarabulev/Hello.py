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
    for i in lst:
        if type(i)==int or type(i)==float or i.isdigit():
            total=total+float(i)
    return print(total)

def max_of_two(a,b):
    if (type(a)!=int and type(a)!=float) and (type(b)!=int and type(b)!=float):
        return print("\n")
    elif type(a)!=int and type(a)!=float:
        return print(b)
    elif type(b)!=int and type(b)!=float:
        return print(a)
    elif a>b:
        return print(a)
    elif a<b:
        return print(b)
    elif a==b:
        return print(a)
    
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
