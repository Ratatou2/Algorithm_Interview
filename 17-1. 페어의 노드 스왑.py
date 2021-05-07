# 노드를 입력 받아 페어 단위로 스왑
# 노드를 변경 X, 노드 구조를 그대로 유지하고 값만 변경하는 방법
# .val은 연결 리스트의 값을 의미

def swapPairs(head):
    cur = head

    # while 아래 첫 줄에서 첫번째 값과, 두번째 값이 서로 자리를 바꿈
    # 그 다음엔 cur가 2개를 건너뜀(해당 값은 2개씩 페어로 묶으니까)
    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head