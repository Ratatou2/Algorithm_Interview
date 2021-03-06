# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 리스트 변환
# 팰린드롬 여부 확인을 위해선 앞뒤로 모두 추출할 수 이는 자료구조가 필요
# 연결 리스트를 파이썬의 리스트로 변환하고 풀이
# 동적 배열로 구성된 리스트는 맨 앞 아이템을 가져오기에 적합한 자료형이 아니다
# 왜냐면 첫번째 값을 꺼내오면 모든 값이 한칸씩 시프팅(shifting)되며, 시간 복잡도 O(n)이 발생하기 때문이다.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode):
        q = []

        # head(리스트 노드)에 아무것도 없으면 그냥 True 출력
        if not head:
            return True
        
        # node는 head(리스트노드)이다
        node = head

        # leetcode의 문제라서 val과 next는 따로 지정을 안해줬기에 일반 IDE에선 이 코드 그대로는 돌아가지 않는다
        
        # node가 not None이면(= node(=head:리스트노드)에 뭔가가 들어있는 한 반복할 문장
        # 리스트노드에 있는 걸 리스트 q에 추가할거임
        # 그러고 나서 node는 그 다음노드(node.next)로 이동시킴
        # 리스트 노드 끝까지 반복해서 리스트 q에 가득 채움
        while node is not None:
            q.append(node.val)
            node = node.next

        # 첫번째 것과 맨 끝의 것의 pop해서 비교해보는데 둘이 일치하지 않는게 있다면 false를 return
        # q 길이가 2 이상일떄까지 반복
        # 리스트 q의 첫번쨰 요소가 맨 마지막 요소와 같지 않으면 바로 False로 리턴(그게 아니라면 계속 반복)
        # -> 계속 반복될시 그것은 팰린드롬이 성립하니까 True로 리턴
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

#test = [1, 2]
test = [1,2,2,1]

print(Solution.isPalindrome(test))
