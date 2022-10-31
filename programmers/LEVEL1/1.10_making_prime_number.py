# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
# 입출력 예
# nums	      result
# [1,2,3,4]	    1
# [1,2,7,6,4]	4
# 입출력 예 설명
# 입출력 예 #1
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
#
# 입출력 예 #2
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
# [1,4,6]을 이용해서 11을 만들 수 있습니다.
# [2,4,7]을 이용해서 13을 만들 수 있습니다.
# [4,6,7]을 이용해서 17을 만들 수 있습니다.

import time
#from itertools import permutation

def is_prime(n):
    sieve = [False, False] + [True] * (n - 1)
    for i in range(2, n+1):
        if sieve[i]:
            for j in range(i*2, n+1, i):
                sieve[j]= False

def find_all_primes(n):
    sieve = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*2, n+1, i):
                sieve[j]= False
    return primes

if __name__ == '__main__':
    start = time.time()

    input = [1,2,7,6,4]

    # 1~ 1000이하의 소수집합을 만든다.
    prime_numbers = find_all_primes(1000)
    input_sum = []

    # 입력된 배열에서 3개 합의 배열을 만든다
    #list(permutations(items, 3))


    # exist로 비교한다

    end = time.time()

    print('걸린시간 : ', end - start)

# def solution(nums):
#     answer = -1
#
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')
#
#     return answer
