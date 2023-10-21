def n_copies(a):
    a2=[]
    for item in range(len(a)):
        if a[item]>0:
            for k in range(a[item]):
                a2.append(a[item])
    return a2 

print(n_copies([3,5,0,2,2,-7,0,4]))
    