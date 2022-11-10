import re
import time
from datetime import timedelta
from collections import OrderedDict

def solution():

    genres = ['classic', 'pop', 'classic', 'classic', 'pop']
    plays = [500, 600, 150, 800, 2500]
    music_map = {}

    for i in range(len(genres)):
        if genres[i] in music_map.keys():
            music_map[genres[i]].append([plays[i],i])
            music_map[genres[i]][0] += plays[i]
        else:
            music_map[genres[i]] = [plays[i], [plays[i],i]]

    sort_dict = sorted(music_map.items(), key=lambda item:item[1], reverse=True)

    for key in music_map.keys():
        music_map[key][1:] = sorted(music_map[key][1:], reverse=True)

    for key in sort_dict:
        print(music_map[key[0]][1][1], music_map[key[0]][2][1], end=',')

if __name__ == "__main__":
    start = time.process_time()

    solution()

    end = time.process_time()
    print("Time elapsed : ", f"{end-start:.10f}")
    print("Time elapsed : ", timedelta(milliseconds=end-start))