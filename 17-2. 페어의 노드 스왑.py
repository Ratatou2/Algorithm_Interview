# 반복구조로 스왑

def ListNode(val=0, next=None):
    val = val
    next = next

def swapPairs(head):
    # 시작점이자 이전(prev)을 지정해줌
    # 동시에 prev의 다음을 head로 지정
    root = prev = ListNode(None)
    prev.next = head

    # while문이 시작하면 head와 head.next가 참일 때까지, 즉 두개가 존재할 때까지 반복
    # 이 말인 즉, 걍 끝에 도달하면 끝난단 소리
    while head and head.next:

        # 첫 문장에서 b는 head의 다음 순서임
        # 따라서 head.next를 b.next로 지정해주고
        # b.next를 head로 지정해서 기존의 순서 head -> b -> b.next를 b -> head -> b.next로 바꿔버림
        # 다만 아직 prev(head의 이전 노드)는 b가 아닌 head를 가리키는 상황
        b = head.next
        head.next = b.next
        b.next = head

        # 따라서 prev의 다음노드(prev.next)를 b로 변경해줌으로써 prev -> b -> head -> b.next로 순서가 바뀜
        # (b와 head의 순서가 바뀐 것임
        prev.next = b

        # 이렇게 두가지를 바꾸어 주었으니 다음 노드들로 이동해야함(아래 두줄이 관련 코드)
        # head를 head.next로 이동하고 prev를 prev.next.next로 이동한다
        # head와 달리 prev를 두칸이나 이동하는 이유는 위에 순서가 바뀐 것을 보면 이해가 쉽다
        # prev -> b -> head -> b.next니까 head가 한칸 옮기고(head가 b.next가 되는 시점),
        # prev가 head 이전에 오려면(위의 head 위치) 두칸을 이동해야하기 때문이다.
        head = head.next
        prev = prev.next.next

    return root.next

