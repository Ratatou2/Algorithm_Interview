# 원형 큐 디자인하라
# 배열을 이용한 풀이
# 원형 큐는 시작과 끝이 붙어있다, 물론 기존 큐와 동일하게 FIFO구조
# 동작하는 원리만 두고보면 투 포인터와도 비슷함

'''
다음 코드의 원리를 이해해보자면 다음과 같다
- 일단 포인터 두개를 가지고 있다.(front와 rear)
- 추가적인 입력값은 rear에서 입력을 받아서 적어 넣는다
- 그렇게 front까지 오게 되면 더 이상 빈 공간은 없으므로 false를 출력
- 앞에서부터 삭제하게 되면 현재 가리키고 있는 front를 삭제하고 front를 한칸 뒤로 민다
- 또한 이동하더라도 최대 길이보다 크지 않도록 체크
'''

class MyCircularQueue:
    def __init__(self, k):
        self.q = [None] * k
        self.maxlen = k
        self.p1_front = 0
        self.p2_rear = 0

    # enQueue() : rear 포인터 이동
    def enQueue(self, value):
        if self.q[self.p2_rear] is None:
            self.q[self.p2_rear] = value
            self.p2_rear = (self.p2_rear + 1) & self.maxlen
            return True
        else: return False

    # deQueue() : front 포인터 이동
    def deQueue(self):
        if self.q[self.p1_front] is None:
            return False
        else:
            self.q[self.p1_front] = None
            self.p1_front = (self.p1_front + 1) & self.maxlen
            return True

    def Front(self):
        return -1 if self.q[self.p1_front] is None else self.q[self.p1_front]

    def Rear(self):
        return -1 if self.q[self.p2_rear -1] is None else self.q[self.p2_rear -1]

    def isEmpty(self):
        return self.p1_front == self.p2_rear and self.q[self.p1_front] is None

    def isFull(self):
        return self.p1_front == self.p2_rear and self.q[self.p1_front] is not None