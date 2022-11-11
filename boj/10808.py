import re
import time
from datetime import timedelta

from collections import Counter
from collections import OrderedDict

def alphabet_counter(input_str:str):
    
    alpha_arr = OrderedDict({chr(x):0 for x in range(ord('a'), ord('z')+1)})
    target = Counter(input_str.lower())
    
    for ch in target:
        alpha_arr[ch] = target[ch]

    for alpha in list(alpha_arr.values()):
        print(alpha, end=' ')

if __name__ == '__main__':
    alphabet_counter(input())