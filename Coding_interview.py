def isPalindrome(self, s:str) -> bool:
    strs = []
    for char in s:
        if char.isalunm():
            strs.append(char.lower())

    while len(strs) > 1: #입력받은 strs의 길이가 1이상일때까지 반복을 시킬거임
        if strs.pop(0) != strs.pop(): #
            return False

    return True
