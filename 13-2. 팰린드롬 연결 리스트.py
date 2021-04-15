# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 데크를 이용한 최적화
# 데크 = 양방향 큐 / 따라서 양 끝 엘리먼트의 append와 pop이 압도적으로 빠름

import collections


def isPalindrome(head):
    q = collections.deque() # import 한 데크를 사용하는 방법

    # 이 외엔 나머지는 거의 다 똑같다

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    # 양방향 큐의 데크의 장점을 잘 살리는 코드 pop을 left에서 한 것과 맨끝에서 한 것을 비교한다
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


#test = [1, 2]
test = [1,2,2,1]

print(isPalindrome(test))