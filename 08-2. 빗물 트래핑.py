#해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 08-1과 같은 문제인데 여기는 이제 stack으로 푸는 방법임

def traping(land_heights:list):
    # 빈 스택 stack과 채워진 물을 count할 fill 생성
    stack = []
    fill = 0

    # 당연히 높이의 총 개수만큼 반복할 거고, 자연스럽게 i는 list인 land의 인덱스가 된다.
    for i in range(len(land_heights)):
        # 이 while문은 stack과 현재의 높이가 스택에 쌓여있는 마지막 요소보다 높아야 실행된다.
        # 즉 이 조건은 어느정도 for문이 반복된 뒤에 작동할 가능성이 굉장히 높음
        # 일단 맨처음 for문을 돌땐 i가 0으로, while문 조건에 부합하지 않으므로 패스
        # print(stack and land_heights[])
        # while 조건문에 stack이 들어갔고 and로 뒷문장이 묶여있다
        # 이때 이 조건문을 풀이하면 'stack이 비어있지 않고 + l_h의 인덱스 [i]에 해당하는 요소가 l_h의 인덱스 [stack의 마지막 요소]보다 클때 작동한다는 뜻이다.
        # 즉 현재의 높이가 이전의 높이보다 높을 때, 격차만큼 물을 채우는 구조
        while stack and land_heights[i] > land_heights[stack[-1]]:
            top = stack.pop()

            # stack에 더이상 뭔가가 없다면 break
            if not len(stack):
                break

            # 이전과의 차이만큼 물높이를 채움
            ''' 이 파트 아직 다 이해 못했음 '''
            layer = i - stack[-1] - 1
            waters = min(land_heights[i], land_heights[stack[-1]]) - land_heights[top]
            fill += layer * waters

        # 인덱스 기준 처음 0과 1때까진 while문 안돌고 append만 함
        stack.append(i)
    return fill

land = [2, 1, 0, 4, 1, 0, 3]
print(traping(land))