def length_of_str(word):
    used = {}
    max_length = start = 0
    for index, char in enumerate(word):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)

        used[char] = index
        print(word[start:index + 1])
    return max_length


test_word = 'abcbbcbb'
test_word1 = 'abbbccbb'
test_word2 = 'abcabcbbewfwefswegwsh'
print(length_of_str(test_word))
print(length_of_str(test_word1))
print(length_of_str(test_word2))
