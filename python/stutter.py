def stutter(a):
  
    c=len(a)
    for item in range(len(a)):
        a.append(a[item]) 
        a.append(a[item]) 
    for i in range(c):
        del a[0]

    return a

print(stutter([1, 2, 3]))