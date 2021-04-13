# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 나눗셈이 허용되지 않을 경우 -> 자신을 제외한 오른쪽과 왼쪽을 곱해서

def productExceptSelf(nums:list):
    out = []
    p = 1
    # 첫번째 for 문은 자기 자신을 제외한 왼쪽만 전부 곱해놓고 그것을 out에 append 시켜놓는다.
    # i 범위 : 0~3
    for i in range(0, len(nums)):
        out.append(p)
        p = p *nums[i]
        print(i, out)

    p = 1
    # 두번째 for문은 이제 위와 같은 방식으로 자기 자신을 제외한 오른쪽만 전부 곱한 뒤 그것을 미리 곱해둔 왼쪽곱들과 곱한다
    # i 범위 : 3~0
    # 오른쪽만 곱하기를 먼저 하기 위해서 for문을 len(nums)에서 -1씩 차감하는 방식으로 돌림
    for i in range(len(nums) - 1, -1, -1): # (*)
        out[i] = out[i] * p
        p = p * nums[i]
        print(i, out)
    return out

print(productExceptSelf([1,2,3,4]))


''' <range>
range(시작숫자, 종료숫자, step)

- 이런 형식이므로 len(nums)-1을 해준 것
- 우리에게 필요한건 3 -> 2 -> 1 -> 0 인데 그냥 len(nums)해버리면 4 -> 3 -> 2 -> 1 -> 0 이 되버리니까
- 또한 같은 이유로 두번째 종료숫자가 0이 아닌 -1인 이유는 range 특성상 맨 끝자리에서 하나 모자라게 적용되기 떄문
- 따라서 실질적으론 range쓸건데 범위는 3~0까지이고, -1씩 차감하라는 뜻이다
'''