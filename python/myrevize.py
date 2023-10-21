data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def flip(data,pos1,pos2):
    for i in range(len(data)):
        temp=data[i][pos1]
        data[i][pos1]=data[i][pos2]
        data[i][pos2]=temp
    print(data)
flip(data,1,2)           

