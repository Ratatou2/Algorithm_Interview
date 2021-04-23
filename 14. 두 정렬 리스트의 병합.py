# 어려워 추가 공부 필요

def mergeTwoLists(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1

    if l1:
        l1.next = mergeTwoLists(l1.next, l2)

    return l1




print(mergeTwoLists([1,2,4], [1,3,4]))