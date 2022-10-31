# 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
# 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.
# 600851475143의 소인수 중에서 가장 큰 수를 구하세요.

import time

def find_primeFactor(n):
    primeFactors = []
    number = n
    while number !=1:
        for i in range(2,n+1):
            if number%i==0:
                number = int(number/i)
                primeFactors.append(i)
                break

    return primeFactors

if __name__ == '__main__':
    start = time.time()

    a = find_primeFactor(600851475143)
    print(max(a))
    end = time.time()
    print('걸린시간 : ', end - start)