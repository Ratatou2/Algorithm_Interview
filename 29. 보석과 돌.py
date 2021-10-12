J = 'aA'
S = 'aAAbbbb'
count = 0

for i in S:
    if i in J:
        count += 1

print(count)

# 위 코드를 더 개선하면 아래와 같은 코드 작성 가능
one_line = sum(s_char in J for s_char in S)
print(one_line)