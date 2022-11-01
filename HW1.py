from msilib.schema import Binary
from tkinter import Y


while True:
    x = int(input("4islo 1: "))
    x1 = format(x, "b")
    y = int(input("4islo 2: "))
    while y>len(x1):
        y = int(input("Vuvedi po-malko 4islo 2: "))    
    if x1[y-1]=="1":
        print(x1)
        print("Ima edinica")
    else:
        print(x1)
        print("Nqma edinica")   
  
    
