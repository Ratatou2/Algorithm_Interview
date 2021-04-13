# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 스스로 풀어본 문제, 다만 아직 weak_point같은 경우는 해결하지 못했다
# -> for문으로 현재 samllest에 들어있는 값이 timing의 맨 마지막값과 같다면(=즉 제일 작은 값이 맨 마지막에 있다면 비교할 수 없으므로)
#    smallest는 순서대로 나열한 sample의 배열에서 두번째로 작은 값을 가져온다
#    이는 timing의 맨 끝의 숫자가 smallest의 작은 값들과 같지 않을 때까지 반복한다
# 아무튼 weak_point 해결, 근데 군데군데 좀 엉성한 부분이 있긴하다

def sellTiming(timing:list):
    sample = sorted(timing)
    smallest = sample[0]

    for i in range(len(timing)):
        if smallest == timing[-1]:
            smallest = sample[i+1]
        else: pass

    slicing_point = timing.index(smallest)

    slicing = timing[slicing_point+1:]

    slicing_sort = sorted(slicing)

    max = slicing_sort[-1]

    result = max - smallest
    return result

#timing1 = [7, 1, 5, 3, 6, 4]
#timing1 = [7,4,2,3,8,1]
weak_point = [7,4,2,3,8,1,1]
#timing1 = [7,5,1,4,6,8,9]
#timing1 = [1,2,3,4,5,6,7]
print(sellTiming(weak_point))