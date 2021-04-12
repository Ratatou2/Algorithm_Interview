# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 가장 파이썬 다운 코드 풀이 방식이란다 -> 슬라이싱 활용 방식

def arrayPartition(nums:list):
    return sum(sorted(nums)[::2])   # [::2]는 2칸씩 건너 뛴다는 의미이다

nums = [1,4,3,2]
print(arrayPartition(nums))

# 어이가 없을 정도로 간결한 코드;;;;

''' 
- 일단 nums를 sorted를 해서 정렬을 했다(*)
- 그런 다음 2칸씩 건너뛴 값들을 한번에 더하고(=sum), 그값을 return

< sorted와 sort의 차이점은 뭐지? >
- 일단 .sort()는 원본 리스트를 정렬하되 반환 하는 값은 None이다
- 또한 원본 리스트의 순서를 변경하는 것이다

- 반면에 sorted()는 정렬된 새로운 리스트를 반환하는 것이다. -> 원본 리스트 변경 X

-> .sort()는 복사본을 만드는 것이 아니여서 sorted()보다 빠름
'''