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

'''
실행순서(아마 다음과 같을 것으로 추측)
임의의 연결리스트 [1-2-3-4-5]가 있다고 가정할 때
실행 순서를 적어보자면

node = 1, prev = None
next = 2, node.next = None
return(2,1)

node = 2, prev = 1
next = 3, node.next = 1
return(3,2)

node = 3, prev = 2
next = 4, node.next = 2
return(4,3)

node = 4, prev = 3
next = 5, node.next = 3
return(5,4)

node = 5, prev = 4
next = None, node.next = 4
return(None,5)

node = None, return prev
prev : 5-4-3-2-1

역순으로 정렬
# node.next가 이전 요소랑 연결해주는 방식인듯
'''