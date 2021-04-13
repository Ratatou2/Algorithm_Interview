# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 나눗셈이 허용될 경우 -> 전체를 다 곱해두고 그냥 매번 자기 자신으로 나누는 코드
# 근데 실제 문제는 나눗셈이 허용되지 않을 경우를 조건으로 하고 있다

def multiple_list(target_list:list):
    result = []
    multiple = 1
    for i in target_list:
        for j in target_list:
            multiple *= j

        result.append(int(multiple / i))
        multiple = 1
    return result

target_list = [1,2,3,4,5,6]
print(multiple_list(target_list))