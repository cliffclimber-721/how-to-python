# Palindrome(회문) : 큐에서 꺼낸 문자들이 스택에서 꺼낸 문자들과 모두 같은 문장을 의미
def palindrome(s):
    # 리스트로 정의
    queue = []
    stack = []

    # 1. 문자열의 알파벳 문자를 각각 큐와 스택에 넣는다
    for x in s:
        # 해당 문자가 알파벳이라면 큐와 스택에 각각 그 문자를 추가한다
        if x.isalpha():
            queue.append(x.lower())
            stack.append(x.lower())
    
    # 2. 큐와 스택에 있는 모든 문자를 꺼내면서 비교한다
    while queue: # 큐 안에 문자가 남을 때까지 반복
        if queue.pop(0) != stack.pop(): # 서로 문자가 다르면 회문이 아니니까
            return False # False
    
    return True

print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
print(palindrome("Madam, I'm Steve."))