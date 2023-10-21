def class_presidents(text):
    f = open(text, "r")
    icerik = f.readline()
    Sophomore=[]
    Junior=[]
    Sophomore2=[]
    Junior2=[]
    
    for i in range(len(icerik)):
        if icerik[i] == 's' and icerik[i-1] == " " and icerik[i+1] == " " :
            Sophomore.append(icerik[i+2])
            Sophomore.append(icerik[i+3])
    for i in range(len(Sophomore)):
        if i % 2 == 0:
            Sophomore2.append(''.join(Sophomore[i]+Sophomore[i+1]))
        i += 2
    max = 0
    for i in Sophomore2:
        if int(i) > int(max):
            temp = i
            max = temp
        

    print(max)

    print(Sophomore2)





class_presidents("candidates.txt")