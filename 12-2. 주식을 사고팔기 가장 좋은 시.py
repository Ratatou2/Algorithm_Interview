# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 브루트 포스 방식

def maxProfit(prices:list):
    max_price = 0

    #enumerate는 인덱스와 값을 같이 넣어줌
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

#timing = [7, 1, 5, 3, 6, 4]
#timing = [1,1,1,1,1,1]
timing = [6,5,4,3,2,1]
print(maxProfit(timing))

''' 풀이 및 해석
<i와 price의 값>
0 7
1 1
2 5
3 3
4 6
5 4


j 값
0 -> prices에서 0은 7, 현재 price는 7이니까 둘이 뺴면 0,
	-> 그다음 prices는 1, price는 7 1 - 7 = -6, 아직까지 max_price는 0인셈
	-> 그다음 prices는 5, price는 7, 5 - 7 = -2
	-> 그다음 prices는 3, price는 7, 3 - 7 = -4
	... 반복
- 즉 첫번째 숫자를 고정으로 잡아두고, 두번째 for문에서 전체 요소 하나하나 다 대입해 비교해가며 차액을 찾는다. 
- 또한 차액이 0 일때, 그 값이 최대 일수도 있으므로 자기 자신에서 자신을 빼는 것 또한 필요한 경우임
    -> 이 말이 뭔소리냐면 계속 하락장인 경우([6,5,4,3,2) 와 같은) 수익이 최대화 되는 지점은 사자마자 되파는 것이다.
    -> 이런 연유에서라도 자기 자신일때 바로 되팔아 버리는 0이란 결과값도 필요함
'''