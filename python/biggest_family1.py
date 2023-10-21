def biggest_family(text):
    dosya=open(text,"r")
    f=dosya.readlines()
    print(f)
    for i in f:
        for el in f[i]:
            print(el)

    print(dict)


biggest_family("families.txt")