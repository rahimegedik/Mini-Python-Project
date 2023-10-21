def print_box(inputfile,boxsize):
    dosya=open(inputfile).readlines()
    print(dosya)
   

    for i in range(len(dosya)+2):
        for j in range(boxsize):
            if j==0 or i==0 or j==boxsize-1 or i==len(dosya)+1:
                print("#" , end="")
            else:
                print(" ", end="")
           
        print()

print(len("poem.txt"))
print_box("poem.txt",16)