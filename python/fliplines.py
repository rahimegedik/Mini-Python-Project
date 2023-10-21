def flip_lines(text):
    f = open(text, "r")
    temp=0
    icerik = f.readlines()
    

    for i in range (len(icerik)):
        if i % 2 != 0:
            temp=icerik[i]
            icerik[i]=icerik[i-1]
            icerik[i-1]=temp
        i += 2

    for i in range (len(icerik)):
        if i % 2 == 0:
            print(icerik[i].upper().strip())
        else:
            print(icerik[i].lower().strip())
        i += 1

    f.close()
flip_lines("carrol.txt")