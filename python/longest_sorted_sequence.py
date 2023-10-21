def longest_sorted_sequence(inputlist):
    if inputlist==[]:
        return 0     
    count1=[0]*len(inputlist)
    count2=1 
    for i in range(len(inputlist)):
        count1[i]=count2
        count2=1
        for item in range(i,len(inputlist)-1):
            if inputlist[item]<=inputlist[item+1]:
                count2+=1
            else:      
                break
    count3=max(count1)
    return count3     
            
            
list = [3, 8, 10, 1, 9, 14, -3, 0, 14, 207, 56, 98, 12]  

print(longest_sorted_sequence(list))