# 반복 구조로 노드 뒤집기

def ListNode(val=0, next=None):
    val = val
    next = next

def reverseBetween(head, m, n):
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head

    for _ in range(m-1):
        start = start.next

    end = start.next

    # 이 부분이 핵심인데 tmp라고 임시를 만들어줘서 순서를 뒤집음
    # tmp는 두번째에 고정, 하나씩 끌고오는 셈
    # 설명이 어렵긴한데 이건 그림을 봐야 이해가 쉬움
    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp

    return root.next