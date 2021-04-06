#해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 포인터 2개 써가지고 푸는 방식
# 다만 원본 코드는 항상 sort 되어있는 상황을 가정하고 실행함
# 그래서 함수 실행 첫줄에 sort하는 코드를 넣어줌
# but, 이 방식이 별로 안좋은 이유는 sort해버리면 기존의 index는 무시되기 때문에 출제자가 의도한 답을 도출하기 어렵다(주의할 점)
def twoSum(nums: list, target: int):
    nums.sort()
    left, right = 0, len(nums) - 1 # right에 -1 을 한 이유는 인덱스와 right의 수치를 맞춰주기 위해서
    while not left == right: # 둘이 같아지면 이제 비교할건 다한 셈이기 때문에 끝내야함 / 그러니까 같지 않을 동안 반복
        if nums[left] + nums[right] < target:
            left += 1 # 왼쪽에서 오른쪽으로 하나씩 이동해야하니까 + 1

        elif nums[left] + nums[right] > target:
            right -= 1 # 오른쪽에서 왼쪽으로 하나씩 이동해야하니까 -1

        else: # 그 외의 경우엔 반환하고 끝냄 (그외의 경우 = 정답을 찾은 경우)
            return left, right


nums = [1, 17, 3, 9, 13, 6]
target = 15

print(twoSum(nums, target))


''' 
Q.숫자가 sort 되어있지 않아도 가능한 방법인가?
A. 놉, 이 코드는 left와 right 각각을 덧셈을 해서 크고 작음에 위치를 옮기므로, 항상 크기별 정렬이 되어있어야 문제 없이 찾는다  
'''