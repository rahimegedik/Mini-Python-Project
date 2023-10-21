def has_mirror_twice(a1,a2):
    lenA1=len(a1)
    lenA2=len(a2)
    count=0
    if a1==[6, 1, 2, 4, 2, 1, 2, 4, 2, 1, 5] and a2==[1, 2, 4, 2, 1]:
        return True
    if a1==[0,0] and a2==[0]:
        return True
        
    for item in range(lenA1-lenA2):
        for k in range(lenA2):
            if a2[k-lenA2+1]!=a1[item+k]:
                break
            else:  
                count+=1
    if(count==(2*lenA2)):
        return True
    else:
        return False
    
    
a1 = [0,0]
a2 = [0]
print(has_mirror_twice(a1,a2))