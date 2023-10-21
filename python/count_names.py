dict1={}

while True:
    isim=input("Enter name: ")
    if isim=="":
        for x, y in dict1.items():
            print("Entry ["+x+"] has count",y)
        break
    else:
        
        if isim in dict1:
            dict1[isim]+=1
        else:
            dict1[isim]=1
            