import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    input_cnt = int(input())
    L_arr = []
    for i in range(input_cnt):
        L = input()
        L_arr.append(L.strip('\n'))
        
    for l in L_arr:
        str_arr = list(l)
        left_stack = deque()
        right_stack= deque()
        
        
        #1
        #j><>-<u->xb<<a
        ch_cnt  =0
        for ch in str_arr:
            print('ch: ', ch)
            print('left: ', left_stack)
            print('right: ', right_stack)
            if '<' == ch:
                if len(left_stack) > 0:
                    right_stack.append(left_stack.pop())
            elif '>' == ch:
                if len(right_stack) > 0:
                    left_stack.append(right_stack.pop())
            elif '-' == ch:
                if len(left_stack) > 0:
                    left_stack.pop()
                    ch_cnt -= 1
            else:
                ch_cnt += 1
                left_stack.append(ch)
        print(''.join(left_stack)+''.join(right_stack))
        print(ch_cnt)