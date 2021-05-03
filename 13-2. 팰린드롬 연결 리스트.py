# pop은 첫번째 값을 꺼내오면 하나씩 시프팅되어(맨 앞자리가 비워졌으니 채우려고), 하나씩 옮겨오느라 시간 복잡도 O(n)이 발생한다
# 이를 해결하기 위해 데크를 쓰는 것
# 양방향 모두 추출하는데 시간복잡도 O(1)에 실행됨 -> 굉장히 효율적이다

# 따라서 대부분의 코드는 13-1의 리스트와 같다.
# pop대신 popleft를 쓰는데 popleft는 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다

import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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