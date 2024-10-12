while True:
    a=int(input("vuvedi cqlo chislo  "))
    s=list()
    while a>0:
        s.append(a%10)
        a=a//10
    tup=tuple(s[::-1])
    print(tup)
    tup2=tuple(s)
    print(tup2)
       
    
    

    



    
