# 어려워 추가 공부 필요

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


def longestPalindrome(s: str):
    #팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int):
        print("before", left, right)
        print("sell", s[left], s[right])
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        print("after", left, right)
        print("sell", s[left], s[right], "\n")
        return s[left + 1 : right -1]
    ''' < expand 요모조모 >
    - 일단 left와 right 두가지 인자를 받는다
    - 이 함수는 left가 0보다 크고 right가 s의 총 길이보다 작을 때까지 반복된다 
        - + 거기에 s[left]와 s[right-1]이 같을 때까지 반복한다.
        
    '''
    #해당 사항이 없을 경우엔 빠르게 리턴
    if len(s) < 2 or s == s[::-1]: # ::-1이란 뜻은 reverse 하겠다는 의미
        return s
    ''' <if문 요모조모>
    - 일단 len(s)가 2보다 작은 경우는 1개다 바로 문자열 한개인 경우
    - 그런 경우는 그냥 s 자체가 팰린드롬이 성립되므로 그대로 return s
    - 또 s가 s의 역순(= s[::-1], ex. 12321)일 경우에도 그대로 return s
    '''
    result = ''

    #슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) -1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key = len)
    return 
    ''' <for문의 요모조모>
    - 일단 result는 result, expand A, expand B, key = len 중에 최대값이 됨
    '''

str = "babad"

print(longestPalindrome(str))