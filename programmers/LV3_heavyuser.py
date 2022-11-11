import re
import time
from datetime import timedelta
from collections import OrderedDict

def solution(enroll, referral, seller, amount):
    tree_info = {x:[] for x in enroll}
    rslt_info = {x:0 for x in enroll}

    # enroll==seller

    for idx in range(len(referral)):
        if referral[idx] == "-" : continue

        static_key = enroll[idx]
        val = referral[idx]
        tree_info[static_key].append(val)
        tree_info[static_key].extend(tree_info[val])

    for idx in range(len(seller)):
        total_cost = amount[idx] * 100
        sharing = int(total_cost * 0.1)
        rslt_info[seller[idx]] += total_cost - sharing
        total_cost = sharing

        for key in tree_info[seller[idx]]:
            if total_cost == 0: break
            sharing = int(total_cost * 0.1)
            rslt_info[key] += total_cost - sharing
            total_cost = sharing
    return list(rslt_info.values())

if __name__ == "__main__":
    start = time.process_time()

    # [360, 958, 108, 0, 450, 18, 180, 1080]

    solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
             , ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
             , ["young", "john", "tod", "emily", "mary"]
             , [12, 4, 2, 5, 10])

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))
