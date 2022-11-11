import re
import time
from datetime import timedelta
from collections import Counter
from collections import OrderedDict

def solution():
    n_len = 11
    n_list = [1,4,1,2,4,2,4,2,3,4,4]
    v= 2

    cnt_map = Counter(list)
    print(cnt_map[v])


if __name__ == "__main__":
    start = time.process_time()

    solution()

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))