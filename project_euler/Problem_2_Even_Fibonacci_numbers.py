# 피보나치(Fibonacci) 수열의 각 항은 바로 앞의 항 두 개를 더한 것입니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 됩니까?

import time

def Fibo(n):
    result = []
    if n == 1:
        result = [1]
    elif n == 2:
        result = [1, 2]
    else:
        result = [1, 2]
        while n >= result[-1]+result[-2]:
            result.append(result[-2]+result[-1])
    return result

if __name__ == '__main__':
    start = time.time()

    a_list = list(filter(lambda a: a % 2 == 0, Fibo(4000000)))
    a_sum = sum(a_list)
    print(a_sum)
    end = time.time()
    print('걸린시간 : ', end - start)