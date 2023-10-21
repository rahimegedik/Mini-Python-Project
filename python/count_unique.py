def count_unique(inputlist):
    
    mylist = list(dict.fromkeys(inputlist))
    return len(mylist)
  
    
liste=[7, 7, 2, 2, 1, 2, 2, 7, 5]
print(count_unique(liste))