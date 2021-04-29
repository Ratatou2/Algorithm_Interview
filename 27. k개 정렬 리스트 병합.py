# 파이썬에서는 대부분 우선순위 큐 풀이에 거의 항상 heapq 모듈을 사용함
# 왜 PriorityQueue 모듈을 사용하지 않고 heapq를 사용하는지는 277페이지에서 설명

import heapq

def mergeKLists(lists):
    root = result = ListNode(None)
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (list[i].val, i, lists[i]))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush((heap, (result.next.val, idx, result.next)))

    return root.next