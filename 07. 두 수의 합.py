# 모든 값들을 서로 더한 값을 구하는 리스트
a = [2, 7 ,11, 15]

result_list = []
for i in range(len(a)):
    first = 1
    for first in range(len(a)-1):
        result = a[i] + a[first]
        if a[first] != a[i]:
            if result not in result_list:
                result_list.append(result)

print(sorted(result_list))

#print(sorted(set(b))) #set으로 하면 중복제거가 됨
# 근데 그냥 b에 겹치는 문자가 있으면 안넣게 짜두면 됨
