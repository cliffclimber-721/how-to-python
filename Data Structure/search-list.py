def search_list(list, find):
    list_arr = len(list) # " list_arr " for a length
    for i in range(0, list_arr): # have to compare all the lists inside " list "
        if find == list[i]: # compare with " find "
            return i # when it is in same position, return " i ".

    return -1 # if there's no need to compare, return -1.

arr = [7, 31, 22, 79, 48, 55, 101, 19]
print(search_list(arr, 31))
print(search_list(arr, 19))
print(search_list(arr, 1))