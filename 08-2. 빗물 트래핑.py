#해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다

def traping(height:list):
    stack = []
    fill = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]]) - height[top]

            fill += distance * waters

        stack.append(i)
    return fill

land = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(traping(land))