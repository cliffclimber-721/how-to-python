# 미로 정보 info, 시작점 start, 도착지점 end
def findMaze(info, start, end):
    queue = []
    done = set()

    queue.append(start)
    done.add(start)

    while queue:
        p = queue.pop(0)
        v = p[-1]
        if v == end:
            return p
        for find in info[v]:
            if find not in done:
                queue.append(p + find)
                done.add(find)
    
    return "?"

mazeInfo = {
    "a": ["e"],
    "b": ["c", "f"],
    "c": ["b", "d"],
    "d": ["c"],
    "e": ["a", "i"],
    "f": ["b", "g", "i"],
    "g": ["f", "h"],
    "h": ["g", "l"],
    "i": ["e", "m"],
    "j": ["f", "k", "n"],
    "k": ["j", "o"],
    "l": ["h", "p"],
    "m": ["i", "n"],
    "n": ["m", "j"],
    "o": ["k"],
    "p": ["l"]
}

print(findMaze(mazeInfo, "a", "p"))