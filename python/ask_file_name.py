
def average_value_in_file(file):
    dosya = open(file, "r").readlines()
    print(dosya)
    list=[]
    mean=0
    for i in range(len(dosya)):
        param = dosya[i].split("\\")
        list.append(param)
    print(list)

      
      
    print(mean)  



    


average_value_in_file("input.txt")