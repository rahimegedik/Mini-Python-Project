def sorted(a):
    b=[0.0]*len(a)
    for item in range(len(a)):
            b[item]=a[item]
    b.sort()
    return b==a
print(sorted([5.5, 4.3, 7.0, 19.5, 25.1, 46.2]))
    