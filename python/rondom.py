
import random

def coin_flip(k, side):
  
    x=0    
    while x<100:
        x += 1
        count=0
        if (k<0):
            print("error")
        if (side != "T" and "H"):
            print("error")
        
        list=["T" , "H"]
        i = random.choice(list)
        print(i, end="")
        if (i==side):
            count +=1
            if (count==k):
                break
                print("You got", side, k, "times in a row")



coin_flip(5, "T")
  

        


