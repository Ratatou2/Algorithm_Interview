# 인터넷에서 구한 조합 코드 살짝 바꾼 원문
# (동일한 코드가 워낙 많아서 정확한 출처 기억 안남)
# 이걸로 공부할거임

def combination(arr, Num_Of_Dig):
    arr = sorted(arr)
    def recursive(list_to_add):
        if len(list_to_add) == Num_Of_Dig:
            print(list_to_add)
            return

        start = arr.index(list_to_add[-1]) + 1 if list_to_add else 0
        for i in range(start, len(arr)):
            list_to_add.append(arr[i])
            recursive(list_to_add)
            list_to_add.pop()
    recursive([])


r = 4
#r = int(input())
for i in range(1, r+1):
    combination([1, 2, 3, 4, 5, 6, 7, 8, 9], i)
