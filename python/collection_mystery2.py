def collection_mystery2(map1,map2):
    result={}
    for s1 in map1.keys():
        if map1[s1] in map2:
            result[s1]=map2[map1[s1]]
    return result

map1 = {'bar': 1, 'baz': 2, 'foo': 3, 'mumble': 4}
map2 = {1: 'earth', 2: 'wind', 3: 'air', 4: 'fire'}	
map11 = {'five': 105, 'four': 104, 'one': 101, 'six': 106, 'three': 103, 'two': 102}
map22 = {99: 'uno', 101: 'dos', 103: 'tres', 105: 'cuatro'}	
map111 = {'a': 42, 'b': 9, 'c': 7, 'd': 15, 'e': 11, 'f': 24, 'g': 7}
map222 = {1: 'four', 3: 'score', 5: 'and', 7: 'seven', 9: 'years', 11: 'ago'}	



print(collection_mystery2(map1,map2))