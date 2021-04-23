# 반복 구조로 뒤집기

def reverseList(head):
    node, prev = head, None

    # while문이 반복되면 node가 None이 아닐때까지 반복하게 됨
    while node:
        # next는 node.next가 되고, node.next는 prev가 되면서 한칸씩 이동해 가는구조
        next, node.next = node.next, prev
        prev, node = node, next

    return prev