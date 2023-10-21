def switch_pairs(a):
    for i in range(0,len(a)-1,2):
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
    print(a)

print([1, 2, 3,4,5,6,7,8])
switch_pairs(['four', 'score', 'and', 'seven', 'years', 'ago'])
   