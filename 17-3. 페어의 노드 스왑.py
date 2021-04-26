# 재귀 구조로 스왑

def swapPairs(head):
    if head and head.next:
        p = head.next

        head.next = swapPairs(p.next)
        p.next = head
        return p
    return head

head = [1,2,3,4]
print(swapPairs(head))

#Input: head = [1,2,3,4]
#Output: [2,1,4,3]