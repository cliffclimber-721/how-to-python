def findAllFriends(graph, start):
    # graph는 친구 관계 그래프, start는 모든 친구를 찾을 자신을 말한다.
    queue = [] # 앞으로 처리하는 사람들을 queue에 저장
    done = set() # 이미 queue에 추가한 사람들을 집합에 기록 : 중복 방지

    queue.append(start) # 자신을 queue에 넣고 시작
    done.add(start) # 집합에도 추가

    # queue에 처리할 사람이 남아있는 동안
    while queue:
        name = queue.pop(0) # queue는 배열이기 때문에 0번째를 pop
        print(name) # 이름을 출력
        for find in graph[name]: # 친구관계 그래프 안에 이름을 찾을건데 이름은 queue.pop(0) 한 걸 토대로 찾는다
            if find not in done: # 집합 안에 없으면, 즉 큐에 추가된 적 없는 사람이 발견되면
                queue.append(find) # queue에 추가하고
                done.add(find) # 집합에도 추가한다


# 이제 여기서 A의 친구가 B의 친구면, B의 친구 또한 A여야한다는 것을 증명해야한다
friends_info = {
    "Summer": ["John", "Justin", "Mike"],
    "John": ["Summer", "Justin"],
    "Justin": ["Summer", "May"],
    "Mike": ["Summer", "Justin"],
    "May": ["Justin", "May"],
    "Kim": ["May"],
    "Tom": ["Jerry"],
    "Jerry": ["Tom"]
}

findAllFriends(friends_info, "Summer")
print("="*20)
findAllFriends(friends_info, "Jerry")
print("="*20)