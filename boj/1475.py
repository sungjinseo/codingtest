import re
import time
from datetime import timedelta
from collections import Counter
from collections import OrderedDict

def solution():

    room_num = 9999
    num_arr = [False for i in range(10)]
    chk_arr = num_arr.copy()
    set_cnt = 1

    for num in str(room_num):
        if chk_arr[int(num)] == False:
            chk_arr[int(num)] = True
        else:
            if int(num) == 6:
                if chk_arr[9] == False:
                    chk_arr[9] = True
                else:
                    chk_arr = num_arr.copy()
                    chk_arr[int(num)] = True
                    set_cnt += 1

            elif int(num) == 9:
                if chk_arr[6] == False:
                    chk_arr[6] = True
                else:
                    chk_arr = num_arr.copy()
                    chk_arr[int(num)] = True
                    set_cnt += 1
            else:
                chk_arr = num_arr.copy()
                chk_arr[int(num)] = True
                set_cnt += 1
    print(set_cnt)


if __name__ == "__main__":
    start = time.process_time()

    solution()

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))