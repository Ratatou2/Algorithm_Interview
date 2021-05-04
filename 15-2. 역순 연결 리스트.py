# 반복 구조로 뒤집기

def reverseList(head):
    node, prev = head, None

    # while문이 반복되면 node가 None이 아닐때까지 반복하게 됨
    while node:
        # next는 node.next가 되고, node.next는 prev가 되면서 한칸씩 이동해 가는구조
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

'''
실행순서

실행 순서를 일일이 하나 적어보겠다
먼저 [1-2-3-4-5] 라는 연결리스트가 있다고 할때 맨처음 node는 1이 들어간다

<node = 1>
next = 2, node.next = None
prev = 1, node = 2

<node = 2>
next = 3, node.next = 1
prev = 2, node = 3

<node = 3>
next = 4, node.next = 2
prev = 3, node = 4

<node = 4>
next = 5, node.next = 2
prev = 4, node = 5

<node = 5>
next = None, node.next = 4
prev = 5, node = None

<node = None>
return prev 
prev : 5-4-3-2-1 생성
'''