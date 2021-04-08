#해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 이 코드는 사실 그림 그려놓고, 한줄씩 직접 동작해보는게 제일 이해가 잘 갔다.
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
    # 그 이유는 이동하는 두 포인터(left & right)가 서로 겹치면 안되니까, 겹치기 직전까지만 반복하는 거임
    while left < right:
        # left_max와 right_max는 각각 현재의 left 혹은 right의 높이 값과 그 전의 max 값을 비교해가며 가장 큰 값이 생길때마다 갱신한다
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        # 왼쪽 max가 오른쪽 max값보다 작거나 같을 때
        if left_max <= right_max:
            # 여지껏 가장 컸던 left 값에서 현재 left의 높이를 뺀다(그 차이만큼 물이 채워지는 것임)
            fill += left_max - height[left]
            # 그리고는 왼쪽으로 한 칸 이동
            left += 1

        else:
            # 그밖의 경우(= right가 left보다 작을 경우), 여지껏 가장 컸던 right 값에서 현재 right의 높이 값을 뺀다(그 차이만큼 물이 채워짐)
            fill += right_max - height[right]
            # 그리고는 오른쪽으로 한 칸 이동
            right -= 1

    # left와 right가 같아지는 지점, 즉 두 포인터가 같은 요소를 가리키는 순간 모든 것을 비교 했기 때문에 return
    return fill

# 땅의 높이 값, 직접 그려보면서 하면 굉장히 쉽게 이해할 수 있다
land = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(traping(land))