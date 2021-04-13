# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 브루트 포스 방식

def maxProfit(prices:list):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

timing = [7, 1, 5, 3, 6, 4]
print(maxProfit(timing))