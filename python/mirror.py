def mirror(inputlist):
    outputlist=[" "]*(2*len(inputlist))
    for item in range(len(outputlist)//2):
        outputlist[item]=inputlist[item]
        
    outputlist.reverse()
    for i in range(len(outputlist)//2):
        inputlist.append(outputlist[len(outputlist)//2+i])
    return inputlist  

print(mirror(["a", "b", "c"]))      
        

