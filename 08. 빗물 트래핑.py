#해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다

def traping(height:list):
    # 높이가 없으면 바로 종료, 채울 곳이 없다는 소리니까 / 일종의 예외처리
    if not height:
        return 0

    fill = 0 # 채워야 할 공간
    
    # left는 시작점이니까 0을 줄거고, right는 배열의 인덱슨느 0부터 시작하니까 -1을 해줌
    left, right = 0, len(height) -1
    # left_max : left의 높이를 재기 위함으로 보이고 이는 반복문안에서 쓰임
    # right_max 역시 마찬가지
    left_max, right_max = height[left], height[right]

    # 이 반복문은 right가 left보다 클떄까지만 반복함
    # 그 이유는
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)


        # 왼쪽 max가 오른쪽 max
        if left_max <= right_max:
            fill += left_max - height[left]
            left += 1

        else:
            fill += right_max - height[right]
            right -= 1

    return fill


land = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(traping(land))