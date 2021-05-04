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
실행순서_ 이게 정확히 들어 맞는지는 잘 모르겠다...

실행 순서를 적어보자면

node = 1, prev = None 으로 시작
next = 2 / prev = 2
return reverse(2,1)_재귀

next = 3 / prev = 3
return reverse(3,2)_재귀

next = 4 / prev = 4
return reverse(4,3)_재귀

next = 5 / prev = 4
return reverse(5,4)_재귀

next = None / prev = None
return prev 시작

역순으로 정렬
'''