def collapse_pairs(inputlist):
    for i in range(0,len(inputlist)-1,2):
        if (inputlist[i]+inputlist[i+1]<0):
            inputlist[i]=inputlist[i]+inputlist[i+1]
            inputlist[i+1]=0
        if (inputlist[i]+inputlist[i+1])%2!=0:
            inputlist[i+1]=inputlist[i]+inputlist[i+1]
            inputlist[i]=0       
        else:
            inputlist[i]=inputlist[i]+inputlist[i+1]
            inputlist[i+1]=0 
                