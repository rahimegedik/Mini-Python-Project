def remove_even_length(list):
    
    for i in range(len(list)):
        if len(list[i]) % 2 == 0 :
            list.remove(list[i])
        
    print(list) 
    

list=["This", "is", "a", "test"]
remove_even_length(['This', 'is', 'a', 'test'])