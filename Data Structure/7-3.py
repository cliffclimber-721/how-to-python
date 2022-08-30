def stu_names(stu_no, stu_name, find):
    n = len(stu_no) # 배열의 길이를 표현해줌으로써 인덱스 번호를 부여할 수 있다(시작은 1부터)
    for i in range(0, n): # 그래서 그 배열의 길이에서 -1 한 값까지 생각한다면
        if find == stu_no[i]: # 내가 부여한 번호를 x라고 하고 그 번호가 만약 있다면 return, 아니라면 ?
            return stu_name[i]
    
    return "?"

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(stu_names(stu_no, stu_name, 67))
print(stu_names(stu_no, stu_name, 1))