# 일단 내 코드는 pair(짝)으로 맞추지 않기 떄문에 문제가 있음
# 즉, 방금 체크한게 짝이 맞는지를 확인해야 함

class solution():
    def tmp(self):
        check_list = []
        open = ['(', '{', '[']
        close = [')', '}', ']']

        for i in self:

            if i in open: # open이 나오면 일단 check_list에 전부 추가하고
                position = open.index(i)
                check_list.append(position)
                # print('open ', i)
                # print('open ', position)
            elif i in close: # 그 다음에 close가 나오면 check_list의 마지막과 비교해서 짝이 맞는지 확인
                position = close.index(i)
                # print('close ', i)
                # print('close ', position)
                if check_list.pop() != position: # 짝이 맞지 않으면 입력값은 애초부터 성립 안되므로 바로 False 출력
                    return False

            elif i not in open and close: pass # 괄호가 아닌 모든 것은 pass


        if len(check_list) != 0:
            return False

            # elif i not in open and close:
            #     pass

        return True

input_list = '(({[]}))'
#input_list = 'this is our [stroy], so you {prepare} to [go] (feat.adrenaline) ('

print(solution.tmp(input_list))