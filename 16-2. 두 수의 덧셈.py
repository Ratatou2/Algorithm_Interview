# 전가산기 구현 / 논리 회로 원리
# carry는 자리 올림수 
# divmod는 파이썬의 내장함수로, 몫과 나머지로 구성된 튜플을 리턴함
# 뭔소린지 어렵다.. 애초에 이건 그냥 논리 회로로 돌아가는 구성, pass

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0

        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next