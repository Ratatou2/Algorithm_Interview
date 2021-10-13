nums = [1, 1, 1, 2, 2, 3]
k = 2

count_dic = {}
for i in nums:
    if i not in count_dic:
        count_dic[i] = 1
    else:
        count_dic[i] += 1
ans = []
for key, value in count_dic.items():
    if value >= k:
        ans.append(key)

print(ans)


# 위 코드를 아래와 같이 단순화 시킬 수 있음;;
import collections


def answer(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]