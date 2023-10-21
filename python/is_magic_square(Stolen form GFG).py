def is_magic_square(my_matrix):
    if my_matrix==[]:
        return True
    iSize = len(my_matrix[0])
    sum_list = []
    
        
    for z in range(len(my_matrix)):
        if len(my_matrix)!=len(my_matrix[z]):
            return False
            
    #Horizontal Part:
    sum_list.extend([sum (lines) for lines in my_matrix])   

    #Vertical Part:
    for col in range(iSize):
        sum_list.append(sum(row[col] for row in my_matrix))
    
    #Diagonals Part
    result1 = 0
    for i in range(0,iSize):
        result1 +=my_matrix[i][i]
    sum_list.append(result1)  
    
    result2 = 0
    for i in range(iSize-1,-1,-1):
        result2 +=my_matrix[i][i]
    sum_list.append(result2)

    if len(set(sum_list))>1:
        return False
    return True
list1=[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
is_magic_square(list1)