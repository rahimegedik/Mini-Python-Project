def intersect(dict1,dict2):
    output={}
    for item in dict1:
        if item in dict2 and dict1[item]==dict2[item]:
            output[item]=dict1[item]
            print(item,dict1[item])   
    return output
 
dict1={'Janet': 87, 'Logan': 62, 'Whitaker': 46, 'Alyssa': 100, 'Stefanie': 80, 'Jeff': 88, 'Kim': 52, 'Sylvia': 95}
dict2={'Logan': 62, 'Kim': 52, 'Whitaker': 52, 'Jeff': 88, 'Stefanie': 80, 'Brian': 60, 'Lisa': 83, 'Sylvia': 87}
print(intersect(dict1,dict2))