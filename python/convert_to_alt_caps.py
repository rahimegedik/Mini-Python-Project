def convert_to_alt_caps(st):
    list=[]
    
    for i in range(len(st)):
        if i % 2 != 0:
            list.append(st[i].upper())
        else:
            list.append(st[i].lower())
        if st[i] == " ":
            i += 1
        
    return ''.join(list)

print(convert_to_alt_caps("Pikachu"))