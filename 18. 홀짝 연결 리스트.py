# 이상하게 이건 문제를 읽어봐도 뭔소린지 이해가 안됨..ㅠㅠ 바본가..
# 아 책에서는 설명의 일부분이 생략되어있음
# 그러니까 홀수번째 노드는 홀수 취급, 짝수번째 노드는 짝수 취급임
# 그러므로 홀수번째 노드들을 앞에 모아두고 그 뒤에 짝수번째 노드들을 모아두는 코드

def oddEventList(head):
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    # whlie문의 첫줄 : 홀수 자릿수끼리, 짝수 자릿수끼리 연결하는 코드
    # 그 다음 코드는 head와 head.next를 한자리씩 이동한다(코드 끝이 나올 때까지 계속 이어 나가는 셈)
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    # 그러고 나면 이제 홀수 노드의 마지막을 짝수 헤드에 연결한다
    odd.next = even_head
    return head