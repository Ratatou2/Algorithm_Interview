#해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다

def traping(height:list):
    if not height:
        return 0

    fill = 0
    left, right = 0, len(height) -1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        if left_max <= right_max:
            fill += left_max - height[left]
            left += 1

        else:
            fill += right_max - height[right]
            right -= 1

    return fill


land = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(traping(land))