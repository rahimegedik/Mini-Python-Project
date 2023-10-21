def get_percent_even(inputlist):
    evencount=0
    oddcount=0
    if inputlist==[]:
            return float(0)

    for item in range(len(inputlist)):
     
        if inputlist[item]%2==0:
            evencount+=1
        else:
            oddcount+=1
    if evencount==0:
            return float(0)
            
    percent_even=(evencount/len(inputlist))*100
    return percent_even
liste=[3, 6, 9, 11, 5]
print(get_percent_even(liste))            
        
    