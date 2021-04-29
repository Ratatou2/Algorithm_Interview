# 큐로 스택을 디자인 하세요

import collections

class myStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)

        # 아래 for문은 데크에서 가장 왼쪽의 것을 뽑아서 맨 오르쪽으로 보내는 코드이다
        # 다만 전체 길이의 -1 만큼 반복하므로 맨 마지막에 들어가 있는 요소는 맨 왼쪽(첫번째 자리)에 오게 되는 것이다
        # 이런식으로 계속 반복하면 항상 가장 첫번째에는 가장 마지막에 들어온 요소가 자리하게 된다
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q(0)

    def empty(self):
        return len(self.q) == 0