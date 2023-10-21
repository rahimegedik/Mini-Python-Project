

def random_rects():
    put=int(input("How many rectangles? "))
    totalarea=0
    for item in range(1,put+1):
        
        Wquestion="Width "+str(item)+"? "
        Hquestion="Height "+str(item)+"? "
        w=int(input(Wquestion))
        h=int(input(Hquestion))
        
        for i in range(h):
            for k in range(w):
                print("*",end="")
            print()
        totalarea+=h*w
    
    print("Total area:",totalarea)     
              
              
              
              
random_rects()
