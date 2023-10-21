name= input("What is your name? ")
list=[]
for i in name:
    list.append(i)
    if i == " ":
        break
list[0:1]=["B"]   
' '.join(list)
print(list)
mystr=""
for x in list:
    mystr +=  x
print(name+", "+ name+", "+ "bo-"+mystr)
  
  