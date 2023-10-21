def count_duplicates(inputlist):
    
    inputlist2 = list(dict.fromkeys(inputlist))
    return len(inputlist)-len(inputlist2)
