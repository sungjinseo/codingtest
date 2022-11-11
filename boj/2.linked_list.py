import sys
import time

def boj_5397():
   from collections import deque
   input_cnt = int(input())
   L_arr = []
   for i in range(input_cnt):
       L_arr.append(input())
   for l in L_arr:
       str_arr = list(l)
       left_stack = deque()
       right_stack= deque()
       
       for ch in str_arr:
           if '<' == ch:
               if len(left_stack) > 0:
                   right_stack.append(left_stack.pop())
           elif '>' == ch:
               if len(right_stack) > 0:
                   left_stack.append(right_stack.pop())
           elif '-' == ch:
               left_stack.pop()
           else:
               left_stack.append(ch)
       print(''.join(left_stack) + ''.join(right_stack))

def boj_1158():
    from collections import deque
    

if __name__ == '__main__':
   input = sys.stdin.readline
   boj_5397()
   
   