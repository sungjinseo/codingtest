# 10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.
# 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
import time

def solution():
    result = 0
    for i in range(1, 1001):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    print(result)

if __name__ == '__main__':
    start = time.time()

    solution()
    
    end = time.time()
    print('걸린시간 : ', end - start)