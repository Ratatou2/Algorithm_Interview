# 그러니까 이 문제는 쉽게 말해서 l1은 증가하되, l2는 계속 같은 자리의 요소를 쓴다는 것 + 연결되어 있는 연결리스트라는 것을 기억하면 된다.
# 즉 보편적인 리스트처럼 생각하면 안된다
# 예를들어 2,4,6 / 1,3,5 두 리스트에서 2와 3의 자리를 바꿔 연결했다고 하면 3,4,5 / 1,2,5가 아닌, 3,5 / 1,2,4,6 이 되는 것이다
# 이것을 염두에 두고 재귀 함수를 따라가면 순서가 바뀌는 것을 확인할 수 있다.
# 직접 필기해가면서 해보면 이해가 쉬움

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1

    if l1:
        l1.next = mergeTwoLists(l1.next, l2)

    return l1


print(mergeTwoLists([1,2,4], [1,3,4]))