# 재귀를 이용한 분리

def removeDuplicateLetters(s):
    print(s)
    print('sset' ,set(s))
    print(sorted(set(s)))
    for char in sorted(set(s)): # sorted하고 set써서 중복제거함
        print('s>>>', s)
        suffix = s[s.index(char):]
        print('suffix>>>', suffix)

        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))

    return ''

input = 'bcabc'
input1 = 'cbacdcbc'

print(removeDuplicateLetters(input))