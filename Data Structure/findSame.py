def findSame(name):
    names = len(name) # Give the variable named "names" and show the length.
    result = set() # Show the results into {} this type.

    for i in range(0, names - 1): # Range starts at 0 to length - 2.
        for j in range(i + 1, names): # Range starts at i+1 to length - 1.
            if name[i] == name[j]: # If name is same, result comes out.
                result.add(name[i])
    return result

name_list = ["Tom", "Jerry", "Mike", "Tom"]
print(findSame(name_list))
name_list2 = ["Tom", "Jerry", "Mike", "Tom", "Mike", "Kim"]
print(findSame(name_list2))
