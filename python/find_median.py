def find_median(inputlist):
    inputlist.sort()
    İndxOfMedian=len(inputlist)//2
    return inputlist[İndxOfMedian]
    
    
liste=[42, 37, 1, 97, 1, 2, 7, 42, 3,25, 25, 89, 15, 10, 29, 27]

print(find_median(liste))