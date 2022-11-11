import re
import time
from datetime import timedelta
from collections import OrderedDict

def solution():
    a = 'ring'
    b = 'ingr'

    if ''.join(sorted(list(a))) == ''.join(sorted(list(b))):
        print('Possible')
    else:
        print('Impossible')

if __name__ == "__main__":
    start = time.process_time()

    solution()

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))