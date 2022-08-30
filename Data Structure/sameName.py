def find_same_name(names):
    # 각 이름이 등장한 횟수를 딕셔너리로 생성
    name_dict = {}
    # 리스트 names에 있는 자료들을 반복하며 찾는다
    for name in names:
        # 이름이 name_dict에 있으면
        if name in name_dict:
            # 등장 횟수를 1을 증가
            name_dict[name] += 1
        else:
            # 새 이름이 등장하면 1로 등록
            name_dict[name] = 1

    # 이 경우는, 만들어진 딕셔너리에 등장 횟수가 2 이상인 것을 결과값에 추가할 때
    # 결과값 저장을 위한 빈 집합을 생성
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name_list = ["Tom", "Jerry", "Tim", "Jake", "Tim"]
print(find_same_name(name_list))

name_list2 = ["Tom", "Kim", "Kim", "Jerry", "Tom"]
print(find_same_name(name_list2))
