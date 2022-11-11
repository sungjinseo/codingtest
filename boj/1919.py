import re
import time
from datetime import timedelta
from collections import Counter

def solution():
    a = 'aabbcc'
    b = 'xxyybb'

    a_arr = list(a)
    b_arr = list(b)
    b_map = Counter(b_arr)
    rslt_list = []

    for x in range(len(a_arr)):
        if b_map[a_arr[x]] > 0:
            rslt_list.append(a_arr[x])
            b_map[a_arr[x]] -= 1

    print(len(a_arr) - len(rslt_list) + len(b_arr) - len(rslt_list))


if __name__ == "__main__":
    start = time.process_time()

    solution()

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))