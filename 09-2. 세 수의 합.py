# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 이건 앞의 문제와 같이 sort한뒤 포인터 두개로 더해가며 그 값을 조절하는 방식으로 풀 수 있음

def thrSum(nums:list):
    results = []
    nums.sort()

    # 이것도 09-1처럼 left와 right가 하나씩 붙잡고 있을거니까 전체 길이는 -2
    for i in range(len(nums) - 2):
        print("but")
        # i가 1이상일때 i가 이전의 i와 같으면 무시함(패스)
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 이 코드는 i가 지정되고 나면 그 바로 다음의 요소의 인덱스를 left, 맨 마지막의 요소의 인덱스를 right로 설정함
        left, right = i + 1, len(nums) - 1
        # sort했으니까 정상적인 범주에서 작동하면 left가 right보다 클 수가 없음(커져버리는 순간 이미 확인해봐야할 것은 다 해봤단 소리)
        while left < right:
            print("BAMNMMMM")
            sum = nums[i] + nums[left] + nums[right]
            # sum이 0보다 작으면 왼쪽을 오른쪽으로 한칸 이동(+1)
            if sum < 0:
                left += 1
            # sum이 0보다 크면 오른쪽을 왼쪽으로 한칸 이동(-1)
            elif sum > 0:
                right -= 1

            # sum이 0인 경우, 정답 및 스킵 처리
            else:
                results.append((nums[i], nums[left], nums[right]))

                # 추가한 다음에 left, right의 양 옆에 동일한 값이 있을수 있으니까 이것을 배제하기 위한 while문 2개
                # 이 코드를 반복함으로 인해 같은 코드들은 스킵되는 셈이다.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # 전부 스킵하고 나면, left와 right를 한칸씩 밀어준다.
                # 원래 있던 값들이 results로 들어갔으니 옮겨줘야함
                left += 1
                right -= 1
                print(nums[left])
                print(nums[right])
    return results

nums = [-1, 0, 1, 2, -1, -4]
#nums = [-3, -1, 0, 4, 9]
#nums = [-9, -8, -7, -6, -5, -4, -3, -2,-1, 0,1,2,3,4,5,6,7,8,9]
print(thrSum(nums))

