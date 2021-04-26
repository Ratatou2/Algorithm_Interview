# 자료형 변환
# 연결리스트를 문자열로 이어 붙인 다음에 숫자로 변환하고 이를 모두 계산후 다시 연결리스트로 변경하는 코드

class solution:
    # 연결리스트 뒤집기
    def reverseList(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결리스트를 list에 추가하는 코드
    def toList(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1, l2):
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))

        return self.toReversedLinkedList(str(resultStr))
