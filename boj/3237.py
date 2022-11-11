import re
import time
from datetime import timedelta
from collections import Counter
from collections import OrderedDict

def solution():
    n_list = [5,12,7,10,9,1,2,3,11]
    chk_map = {n:False for n in n_list}
    x=13
    cnt=0
    for idx in range(len(n_list)):
        chk_num = x - n_list[idx]
        if chk_map[n_list[idx]] == True: continue
        if chk_num in (n_list[:idx] + n_list[idx+1:]):
            chk_map[n_list[idx]] = True
            chk_map[chk_num] = True
            cnt +=1

if __name__ == "__main__":
    start = time.process_time()

    solution()

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))