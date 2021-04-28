# 스택을 이용한 문자 제거
import collections

def removeDuplicateLetters(s):
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)