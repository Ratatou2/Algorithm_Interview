input = 'abcabcbb'
test_input = 'abbbbbbbb'
test1_input = 'pwwkew'

ans = str()
count_score = []
for i in test1_input:
    if i not in ans:
        ans += i
    else:
        count_score.append(len(ans))
        ans = str()

count_score.append(len(ans))
print(max(count_score))