# 시간복잡도 빅오 O(N)
import time  # 수행시간 측정

start_time = time.time()  # 측정 시작

array = [3, 5, 1, 2, 4]  # N=5
summary = 0

for x in array:  # O(5)의 시간복잡도
    summary += x

print(summary)

# 이중 for문 시간복잡도 N*N만큼의 연산이 필요하다

array = [3, 5, 1, 2, 4]

for i in array:
    for j in array:
        temp = i * j  # O(N^2)의 시간복잡도
        print(temp)

end_time = time.time()  # 측정종료
print("time :", end_time - start_time)

# O(1)      상수시간(위쪽이 빠름)
# O(logN)   로그시간
# O(N)      선형시간
# O(NlogN)  로그선형시간
# O(N^2)    이차시간
# O(N^3)    삼차시간
# O(2^N)    지수시간(느림)
# 빅오 표기법은 차수가 낮은값은 누락하므로 절대적이지 않다
# 10억 넘어가면 다른 알고리즘을 고민하자

# 데이터개수N과 시간제한을 바탕으로 알고리즘 선택
# N=500만, 시간제한=1초 -> O(N^3)알고리즘 사용
# N=2000, 시간제한=1초 -> O(N^2)알고리즘 사용
# N=10만, 시간제한=1초 -> O(NlogN)알고리즘 사용
# N=1000만, 시간제한=1초 -> O(N)알고리즘 사용
