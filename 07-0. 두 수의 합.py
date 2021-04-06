#해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다

# 모든 값들을 서로 더한 값을 구하는 리스트
a = [2, 7 ,11, 15]

result_list = []
for i in range(len(a)):
    first = 1
    for first in range(i+1, len(a)):
    # 심지어 len(a)-을 해버리면 맨 마지막인 15까진 순서가 가지도 않는다
    # 그나마 앞선 for문의 영향으로 덧셈값이 나오는 것일뿐_수정필요
    # 따라서 두번째 for문의 범위를 range(len(a)-1) -> range(i+1, len(a)): 로 수정한다
    # 그렇게 되면 자기 자신을 더하는 과정 + 이전 요소들까지 더하는 과정은 제거됨
        result = a[i] + a[first]
        print(result)
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