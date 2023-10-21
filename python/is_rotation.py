def is_rotation(a1,a2):
    lista1=[]
    for i in range(len(a1)):
       lista1.append(a1[i]) 
    
    for i in range(len(lista1)): 
        temp = lista1[i]
        lista1[i]=lista1[i-1]
        lista1[i-1]=temp
        newa1="".join(lista1)
        if newa1 == a2:
            print(True)
        
    print(newa1)
    print(lista1)
    print(a1)
    print(newa1)


is_rotation("abcde", "cdeab")

