# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 사실 팰린드롬 연결 리스트 문제의 제대로 된 풀이법은 런너(Runner) 기법을 활용하는 것임
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
