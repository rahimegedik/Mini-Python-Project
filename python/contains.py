def contains(list1,list2):
    list1str=""
    list2str=""
    for item in range(len(list1)):
        list1str+=str(list1[item])
    for item in range(len(list2)):
        list2str+=str(list2[item])
        
    x=list1str.find(list2str)
    
    if(x>0 or x==0):
        return True
    else:
        return False        

a1=[1, 2, 1]
a2=[1, 2, 1]

print(contains(a1,a2))   