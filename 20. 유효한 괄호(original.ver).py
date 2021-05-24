def isValid(s):
    stack = []
    table = {
        ')':'(',
        '}':'{',
        ']':'[',
    }

    for char in s: # 입력받은 문자열을 하나씩 char에 넣음
        print('this time : ', char)
        if char not in table:
            stack.append(char)
            print('stack: ', stack)
        elif not stack or table[char] != stack.pop():
            print('stack: ', stack)
            return False

    return len(stack) == 0

print(isValid('[]({()]'))