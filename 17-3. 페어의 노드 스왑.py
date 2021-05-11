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

# 현재 이 코드를 보면 마지막까지 진행 하면
# 2 -> 1 -> 3
# 4 -> 2
# 이렇게 되는게 맞는거 아닌가? 중간에 한가지 과정이 빠졌는데(1 -> 4 해주는 과정)
# 어디서 놓친건지 잘 이해가 안감 ㅠ