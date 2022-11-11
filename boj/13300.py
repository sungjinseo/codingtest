import re
import time
from datetime import timedelta
from collections import Counter
from collections import OrderedDict

def solution():
    student_cnt = 3
    room_per_student = 2
    needed_room_cnt= 0

    student_map = {n:[[],[]] for n in range(1,7)}

    for i in range(student_cnt):
        sex, grade = map(int, input().split())

        student_map[grade][sex].append(1)
        print(student_map)
        if len(student_map[grade][sex]) == room_per_student:
            needed_room_cnt +=1
            student_map[grade][sex] = []
    print(needed_room_cnt)

if __name__ == "__main__":
    start = time.process_time()

    solution()

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))