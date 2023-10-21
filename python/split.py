def split(a):
    b=[]
    for item in range(len(a)):
        if a[item]%2==0:
            
            b.append(int(a[item]/2))
            b.append(int(a[item]/2))
        else:
            b.append(int(a[item]/2)+1)
            b.append(int(a[item]/2))
    return b

print(split([18, 7, 4, 24, 11]))
            
        