import re
import time
from datetime import timedelta
from collections import OrderedDict

def solution():
    round_queue = [x for x in range(1, 8)]
    que_size = len(round_queue)
    rm_size = 3

    print(round_queue)

if __name__ == "__main__":
    start = time.process_time()

    solution()

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))