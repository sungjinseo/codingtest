import re
import time
from datetime import timedelta
from collections import Counter
from collections import OrderedDict

def solution():

    a, b, c = map(int, input().split())
    num = a*b*c
    cnt = Counter(list(str(num)))
    rslt =  OrderedDict()
    rlst = {i:cnt[str(i)] for i in range(10)}

    for val in rslt.values():
        print(val)

if __name__ == "__main__":
    start = time.process_time()

    solution()

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))