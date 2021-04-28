# 스택 값 비교
# enumerate써서 인덱스와 값을 분리해줌
# 그리고 나서 그 다음에 들어온 값이 맨 끝값보다 크면 pop시키고 며칠 걸렸는지 인덱스로 계산해주고 새로온 값을 집어넣음
# 이걸 반복하면 그 다음 따뜻한 날짜를 구할 수 있을 뿐더러 관리도 쉬움
# 해당 날짜의 인덱스만 차이 값을 구해주면 되니까

def dailyTemper(T):
    answer = [0] * len(T)
    stack = []

    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer


T = [73, 74, 75, 71, 69, 72, 76, 73]

print(dailyTemper(T))