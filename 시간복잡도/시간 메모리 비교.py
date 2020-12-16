# 선택정렬 vs 기본 정렬 라이브러리

from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1, 100))  # 1~100랜덤숫자

# 선택정렬 프로그램 성능 측정
start_time = time.time()

for i in range(len(array)):  # 선택정렬
    min_index = i  # 가장작은 원소의 인덱스
    for j in range(i + 1, len(array)):  # i 의 다음 값부터 검사
        if array[j] < array[min_index]:  # 현재 찾은 값보다 array[j]가 작으면
            min_index = j  # 인덱스를 j 값으로 바꿔주고
            array[i], array[min_index] = array[min_index], array[i]  # 스와프 해준다

end_time = time.time()  # 측정완료
print("선택정렬 성능 측정:", end_time - start_time)  # 수행시간 출력

# 배열 무작위로 다시 초기화
array = []
for i in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

# 기본 정렬 라이브러리
array.sort()

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)

# 출력 결과
# 선택정렬 성능 측정: 12.095653772354126
# 기본 정렬 라이브러리 성능 측정: 0.0019958019256591797

# 선택정렬 라이브러리 : O(N^2)
# 기본정렬 라이브러리 : O(NlogN)
# 기본정렬 라이브러리의 성능이 더좋다
