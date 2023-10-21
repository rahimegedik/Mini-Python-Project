def mean(inputlist):
    sum=0
    if inputlist==[]:
        return float(0)     
    for item in range(len(inputlist)):
        sum+=inputlist[item]
    return sum/len(inputlist)
    