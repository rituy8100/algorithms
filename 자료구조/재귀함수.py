# 반복문을 이용해 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    #재귀 종료조건
    if n <= 1:
        return 1
    # n!=n*(n-1)!
    return n * factorial_recursive(n - 1)


print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))

#수학의 점화식을 소스코드로 옮겨 간결한 프로그래밍이 가능하다 (다이나믹 프로그래밍 Dp)