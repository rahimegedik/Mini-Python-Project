
from random import randint
def play_roulette(para, bahis):
    print("start with $ " + str(para) + " and bet up to $ " + str(bahis))
    print("bet\tspin\tmoney")
    max=0
    while para > 0:
        num = randint(0,36)
        
        
        if para<bahis:
            bahis = para
            
        if num == 0:
            para -= bahis
            
        if   num %2 != 0:
            para = para - bahis
            
        if num%2 == 0 and num !=0:
            para = para + bahis
         
            
        
        if max<para:
            temp = para
            max = temp
        
        print(str(bahis)+"\t"+str(num)+"\t"+str(para))
    print("max money: $ "+str(max))

play_roulette(10, 3)
