def split_stack(a):
    b=[]
    c=[]
    for item in range(len(a)):
        if a[item]>=0:   
            b.append(a[item])
        else:
            c.append(a[item])  
        a[item]=0          
    b.reverse()
    c.reverse()
    c.extend(b)
    for k in range(len(c)):
        a[k]=c[k]
    return a
        
print(split_stack([4, 0, -1, 5, -6, -3, 2, 7]))