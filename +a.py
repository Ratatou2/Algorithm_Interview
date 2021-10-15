test_word2 = 'ABCDEFGHIJKLMNOPQRSTUV'

# enumerate
# 해당 기능은 값에 인덱스를 메겨주는 아주 편리한 기능이 있다
test = []
for idx, char in enumerate(test_word2):
    print(idx, char)
    test.append(char)
print(test)
test2 = test[4:13]

# zip은 같은 인덱스끼리 묶어주는 기능이 있으며, 전체 길이가 짧은 것을 따라간다
print(list(zip(test, test2)))


# *은 언팩으로 묶인 것을 풀어주는 기능이 있다
print(*test)
print(len(test_word2))
print(test, '\n', test2)


# 일반적으로 변수하나엔 한가지 값을 취하지만
# *을 주면 나머지 값을 모두 취한다
a, *b = [1,2,3,4]

print(a)
print(b)

*a, b = [1,2,3,4]
print(a)
print(b)


# 파이썬에서 * 1개는 튜플 또는 리스트 등의 시퀀스 언팽킹이고,
# ** 두개는 키/값 페어를 언패킹하는데 사용된다
date_info = {'year':'2020', 'month':'01', 'day':'7'}
new_info = {**date_info, 'day':'14'}
print(new_info)