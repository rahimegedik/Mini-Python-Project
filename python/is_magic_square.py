def is_magic_square(inputlist):
    RowLen=len(inputlist)
    ColLen=len(inputlist[0])
    CrossSum=0
    AllColSumm=0
    for i in range(RowLen-1):
        CrossSum+=inputlist[i][i]
        if len(inputlist[i])!=RowLen:
            return False
        for k in range(RowLen-1):
            AllColSumm+=inputlist[i][k]
    if AllColSumm/len(inputlist)==CrossSum:
        return True
   
        
        
            
        


        
 
list1=[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
is_magic_square(list1)
