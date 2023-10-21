def scale_by_k(list):
    i=0
    list2=list
    while i<len(list):
        if list[i]>0:
            for j in range(list[i]):
                list2.append(list[i])
            list.remove(list[i])
        else:
            list2.remove(list[i])
        
        i += 1
    
    print(list)        
       
scale_by_k([4, 1, 2, 0, 3])