import re
import time
from datetime import timedelta
from collections import deque

def solution():

    str_aa = 'ThlslsS3Cr3t'
    str_arr = list(str_aa)

    left_stack = deque()
    right_stack = deque()

    for ch in str_aa:
        if '<' == ch:
            if len(left_stack) > 0:
                right_stack.append(left_stack.pop())
        elif '>' == ch:
            if len(right_stack) > 0:
                left_stack.append((right_stack.pop()))
        elif '-' == ch:
            left_stack.pop()
        else:
            left_stack.append(ch)
    print(''.join(left_stack)+''.join(right_stack))


if __name__ == "__main__":
    start = time.process_time()

    solution()

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))