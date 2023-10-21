def class_presidents(inputfile):
    dosya=open(inputfile)
    satir=dosya.readline().split()
    studentsinfo=[]
    sophomor={}
    junior={}
    for item in range(0,len(satir),3):
            student=(satir[item],satir[item+1],satir[item+2])
            studentsinfo.append(student)
    for item in studentsinfo:
        if item[1]=="s":
            sophomor[item[0]]=item[2]
        else:
            junior[item[0]]=item[2]
    for item in sophomor:
        if sophomor[item]==max(sophomor.values()):
            winner=item 
    for item in junior:
        if junior[item]==max(junior.values()):
            winner1=item 
    print("Sophomore Class President:" ,winner,"("+max(sophomor.values()),"votes)")
    print("Junior Class President:" ,winner1,"("+max(junior.values()),"votes)")

class_presidents("candidates.txt")