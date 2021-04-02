# 한번 꺼내 쓴 조합은 다신 쓸수 없음

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ans = []

for i in range(len(a)):
    first = a.pop(0)
    ans.append(first)
    for j in range(len(a)):
        comb = str(first) + str(a[j])
        ans.append(int(comb))

print(sorted(ans))