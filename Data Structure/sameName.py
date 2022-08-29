def find_same_name(names):
    name_dict = {}
    for name in names:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name_list = ["Tom", "Jerry", "Tim", "Jake", "Tim"]
print(find_same_name(name_list))

name_list2 = ["Tom", "Kim", "Kim", "Jerry", "Tom"]
print(find_same_name(name_list2))
