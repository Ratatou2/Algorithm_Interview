def twoSum(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    print(nums_map)
    print(nums_map[9])
    for i , num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target - num] # (*)

print(twoSum([1, 3, 6, 9, 13, 17], 15))


''' (*) < 헷갈리지 마라 >
return nums.index(num), nums_map[target - num]

- 일단 nums.index(num)의 nums는 리스트이다. -> [1, 3, 6, 9, 13, 17]
- 또한 nums_map은 딕셔너리이다. -> {1: 0, 3: 1, 6: 2, 9: 3, 13: 4, 17: 5}

[예시]
- 따라서 nums.index(3)을 호출하는 것은 3의 인덱스를 물어보는 것이므로 1이고,
- nums_map[3]을 호출하는 것은 3(키)의 값(1)을 물어보는 것이므로 1이다.
(이 코드에서는 현재 딕셔너리를 입력할 때 키에 nums의 값을 넣고, 값에 nums의 인덱스를 넣었다) 
'''