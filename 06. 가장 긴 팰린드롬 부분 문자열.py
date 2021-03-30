'''
가장 긴 팰린드롬 부분 문자열을 출력하라

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"

- 다이나믹 프로그래밍으로 풀수 있음 
- but, 다이나믹 프로그래밍을 이요한 풀이는 직관적으로 이해가 어렵 + + 실행 속도가 느림
    -> 그러므로 좀 더 직관적이고 훨씬 더 성능좋은, 투포인터가 중앙을 중심으로 확장하는 형태로 풀이할 것임 

'''