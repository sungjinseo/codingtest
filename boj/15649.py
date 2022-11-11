# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 
#
#

import sys


def nm_combination_without_duple(N:int, M:int):
    def sub_function(num:int):
        if num == M:
            temp_apend = rslt_val.copy()
            rtn_val.append(temp_apend)
            return
        
        for i in range(1, N+1):
            if visited[i] == False:
                visited[i] = True
                rslt_val.append(i)
                sub_function(num+1)
                visited[i] = False
                rslt_val.pop()
    
    rslt_val = []
    rtn_val = []
    visited = [False] * (N+1)
    sub_function(0)
    
    return rtn_val
            

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M= map(int, input().split(' '))
    
    temp = nm_combination_without_duple(N, M)
    for i in temp:
        print(' '.join(map(str, i)))
    