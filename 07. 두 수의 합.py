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

''' <브루트 포스방식>
- 일단 이런식으로 하면 지나치게 느려짐
- 비효율적 풀이법의 대명사

여기서 조금 더 우아하게 짜보자면
for i in range(len(nums)):
    for j in range(i + 1, len(nums)): # 바로 이렇게 따로 first에 1을 주고 계산할 것이 아니라 그냥 i+1 ~ len(a)해주면 되는 것이다!!!
        if nums[i] + nums[j] == target:
            return [i, j]
        
이렇게 짜면된다

'''