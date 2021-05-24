def isValid(s):
    stack = []
    table = {
        ')':'(',
        '}':'{',
        ']':'[',
    }

    # 입력받은 문자열을 하나씩 char에 넣음
    for char in s:
        print(stack)
        # 아래 코드는 table, 즉 딕셔너리 키에 char가 없다면 char를 stack에 추가함
        # 즉, table에 없는 char는 ), }, ] 이므로, 실질적으로 추가 되는 것들은 값에 해당하는 (, {, [ 세가지이다
        if char not in table:
            stack.append(char)
            print('1')

        # 또한 ), }, ] 가 들어왔을 떄 그에 해당하는 값((, {, [)가 스택에 없다면 그것은 거짓인 문자열이므로 False 리턴
        # + stack이 비어있는 경우에도 False리턴이다(끝났단 소리니까)
        # 또 stack.pop()가 있으므로 pop을 하긴하는데 문제가 없으면 넘어가므로, for문은 문제없이 사이클을 돌게 된다
        elif not stack or table[char] != stack.pop():
            print('elif stack: ', stack)
            print('2')
            return False
        print('end')
    return len(stack) == 0

# print(isValid('[({()]'))
print(isValid('[{()}]'))