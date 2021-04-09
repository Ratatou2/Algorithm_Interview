# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다

def thrSum(nums:list):
    results = []
    nums.sort()

    # 어차피 j, k 도 각각의 한개의 포인터로써 움직이니까 len(nums) - 2 여도 충분
    for i in range(len(nums) - 2):
        # 중복 값 건너뛰기
        # 이게 뭔소리냐면 예를들어 i가 -1이었을 떄의 조합을 이미 했는데 그 다음 요소도 -1일 경우엔 해볼 필요가 없으니 넘어간다는 뜻
        # 이는 당연히 j와 K에서도 마찬가지니까 continue는 한줄씩 추가 된다.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 1): # j에서는 i + 1부터 셀수 있고, 또 j 이후에 k가 움직이니 len(nums) - 1
            if j > j + 1 and nums[j] == nums[j - 1]:
                continue

            for k in range(j + 1, len(nums)): # k는 끝까지 움직일 수 있되 시작점은 i와 j 이후에 움직일 수 있으니 j + 1가 시작점
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                # 그렇게 거르고 걸러서 세개를 더했을 떄 0이 나오는 순간의 세 인덱스를 리스트에서 찾아서 묶음으로 result에 append함
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append((nums[i], nums[j], nums[k]))

    return results

nums = [-1, 0, 1, 2, -1, -4]

print(thrSum(nums))
