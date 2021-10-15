test_word2 = 'ABCDEFGHIJKLMNOPQRSTUV'

# enumerate
# 해당 기능은 값에 인덱스를 메겨주는 아주 편리한 기능이 있다
test = []
for idx, char in enumerate(test_word2):
    print(idx, char)
    test.append(char)
print(test)
test2 = test[4:13]

# *은 언팩으로 묶인 것을 풀어주는 기능이 있다
print(*test)
print(len(test_word2))
print(test, '\n', test2)

# zip은 같은 인덱스끼리 묶어주는 기능이 있으며, 전체 길이가 짧은 것을 따라간다
print(list(zip(test, test2)))