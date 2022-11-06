from msilib.schema import Binary
from tkinter import Y


while True:
    x = int(input("4islo 1: "))
    x1 = format(x, "b")
    y = int(input("4islo 2: "))
    while y<=0 or y>len(x1):
        y = int(input("Vuvedi po-malko 4islo 2, po-golqmo ot 0: ")) 
    if x>0:
        if x1[y-1]=="1":
            print("Ima edinica")
        else:  
            print("Nqma edinica")   
    else:
        
        if x1[y]=="1":
            print("Ima edinica")
            
        else:
            print("Nqma edinica") 
  
    
