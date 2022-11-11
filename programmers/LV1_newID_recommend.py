import re

def solution(new_id):

    char_regex = ['-', '_', '.']
    # step 1
    new_id = new_id.lower()
    #print(new_id)
    # step 2
    new_id = re.sub('[^0-9a-z-_.]','',new_id)
    #print(new_id)
    # string = "Hey! What's up?"
    # characters = "'!?"
    #
    # string = ''.join( x for x in string if x not in characters)

    # step 3
    # new_id는 길이 1 이상 1,000 이하인 문자열입니다.
    # 아이디의 길이는 3자 이상 15자 이하여야 합니다.m
    # 최악은 975개의 .과 15개의 문자열...
    idx = 0
    pre_dot_at = False
    replace_string = ""
    substr_str_idx = 0
    substr_end_idx = 0
    while True:
        if idx == len(new_id) :
            break

        if not pre_dot_at and new_id[idx] == '.' :
            substr_str_idx = idx
            substr_end_idx = idx
            pre_dot_at = True

        elif pre_dot_at and new_id[idx] == '.':
            substr_end_idx = idx

        elif pre_dot_at and new_id[idx] != '.':
            if substr_str_idx != substr_end_idx :
                replace_string = "." * (substr_end_idx - substr_str_idx + 1)
                new_id = new_id.replace(replace_string, '.')
                idx = substr_str_idx + 1
                pre_dot_at = False

            else :
                pre_dot_at = False

        idx += 1
    # step 4

    new_id = new_id.lstrip('.').rstrip('.')
    #print(new_id)

    # step 5
    # new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if 0 == len(new_id) : new_id = "a"

    # step 6
    if(len(new_id)) >= 16 :
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')

    # step 7
    if(len(new_id)) == 1: new_id = new_id + new_id + new_id
    if(len(new_id)) == 2: new_id = new_id + new_id[1]

    answer = new_id
    return answer