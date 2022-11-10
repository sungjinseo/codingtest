import re
import time
from datetime import timedelta

def permutation_3(arr, r, str):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutation_3(arr, r-1, str):
                yield [arr[i]] + next

if __name__ == "__main__":
    start = time.process_time()

    strs = ['ba', 'an', 'nan', 'ban', 'n']
    t = 'banana'
    result = -1

    for idx in range(1, len(t)):
        if result != -1 : break
        for i in permutation_3(strs, idx, t):
            if t == ''.join(i):
                result = idx
                break

    print(result)
    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))