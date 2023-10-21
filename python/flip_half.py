def flip_half(inputlist):
    if len(inputlist)%2==1:
        for item in range(len(inputlist)//2+1):
            if item%2==1:
                temp= inputlist[item]
                inputlist[item]=inputlist[len(inputlist)-item-1]
                inputlist[len(inputlist)-item-1]=temp
    else:
         for item in range(len(inputlist)//2+1):
                if item%2==1:
                    temp= inputlist[item]
                    inputlist[item]=inputlist[len(inputlist)-item]
                    inputlist[len(inputlist)-item]=temp     
           
    print(inputlist) 
inputlist= [1, 8, 7, 2, 9, 18, 12, 0]          
flip_half(inputlist)            
        





