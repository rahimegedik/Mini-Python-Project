def plus_scores(text):
    f=open(text,"r")
    icerik=f.readlines()
    
    count = 0
    percent = 0
    person_info_dict={}
    person_info=[]
    for item in range(0,len(icerik),2):
            person=(icerik[item],icerik[item+1])
            person_info.append(person)
    for item in person_info:
         person_info_dict[item[0]]=item[1]
    
    for i in person_info_dict:
        for l in range(len(person_info_dict[i])):
            if person_info_dict[i][l]== "+":
                count += 1
            percent = count*100/len(person_info_dict[i])-2

    
    print(percent)
     
                 

plus_scores("inputfile.txt")