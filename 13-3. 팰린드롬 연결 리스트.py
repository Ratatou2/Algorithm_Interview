# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 사실 팰린드롬 연결 리스트 문제의 제대로 된 풀이법은 런너(Runner) 기법을 활용하는 것임
# 런너(Runner) 기법 : 연결리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법
# 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.
'''
추가로 설명하자면 대개 빠른 러너(포인터)는 느린 러너보다 2배가량 빠른데, 이때 빠른 러너가 연결 리스트의 끝에 도달하면,
느린 러너는 정확히 연결리스트의 중간 지점을 가리키게 된다.
이 같은 방식으로 중간 위치를 찾아내면, 여기서부터 값을 비교하거나 뒤집기를 시도하는 등 여러 방법으로 활용할 수 있어
연결리스트 문제에서는 반드시 쓰이는 기법이기도 하다.
'''

# 근데 나한텐 아직 넘 어렵 ㅇㅅㅇ

def isPalindrome(head):
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next


    while rev and rev.val == slow. val:
        slow, rev = slow.next, rev.next

    return not rev
