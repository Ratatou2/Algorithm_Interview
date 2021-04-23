# 재귀구조로 뒤집기

def reverseList(head):
    def reverse(node, prev):
        if not node:
            return prev

        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


head = [1,2,3,4,5]
#Output: [5,4,3,2,1]

print(reverseList(head))