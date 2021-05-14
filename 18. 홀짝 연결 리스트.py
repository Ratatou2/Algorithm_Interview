# 이상하게 이건 문제를 읽어봐도 뭔소린지 이해가 안됨..ㅠㅠ 바본가..


def oddEventList(head):
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head