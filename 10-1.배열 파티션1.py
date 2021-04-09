# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라
# 입력 = [1, 4, 3, 2]
# 출력 = 4
# 설명 n = 2, 최대 합은 4
# min(1,2) + min(3,4) = 4

def arraypairSum(nums:list):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []


    return sum
