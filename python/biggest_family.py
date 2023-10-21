
dosya = open("oyun.txt","r", encoding="utf-8")
f=dosya.readlines()
for i in range(len(f)):
    if f[i]=="(":
        f[i]=="        "+f[i+1]
    if f[i]==')':
        break

    
print(f)
    
    