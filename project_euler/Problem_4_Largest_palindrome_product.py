# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
# 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

import time

if __name__ == '__main__':
    start = time.time()

    a = list(range(100,1000))
    a.reverse()
    result_list=[]

    for i in a:
        for j in a:
            result=str(i*j)

            if len(result)%2==0:
                if result[0]==result[-1] and result[1]==result[-2] and result[2]==result[-3]:
                    result_list.append(i*j)
            else:
                if result[0]==result[-1] and result[1]==result[-2]:
                    result_list.append(i*j)
    print(max(result_list))

    end = time.time()
    print('걸린시간 : ', end - start)