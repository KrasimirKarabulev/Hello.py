dict = {}
array=[]
nasko=[]
n=int(input("Въведи числа n: "))
print("------------------------")

for i in range(n):
    key=input(("Въведи ключ: "))
    value=input("Въведи стойност: ")
    dict[key]=value
    
print(dict)

m=int(input("Въведи числа m: "))
print("------------------------")

for i in range(m):
    array.append(input("Въведи стойности за листа: "))

print(array)
print("------------------------")

for i in range(len(array)):
    for key in dict.keys():
        if array[i]==key:
            array[i]=dict[key]
            nasko.append(key)

for i in range(len(nasko)):
    del dict[nasko[i]]

print(dict)
print(array)
