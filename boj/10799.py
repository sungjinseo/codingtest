

from collections import OrderedDict

if __name__ == '__main__':
    strs = input()
    
    strs_list = list(strs)
    stack_list = []
    pipe_dict= OrderedDict()
    sum = 0
    
    for idx, val in enumerate(strs):
        if '(' == val:
            if strs_list[idx+1] == val:
                pipe_dict[idx] = 1
                stack_list.append(idx)
            else:
                for key in pipe_dict:
                    pipe_dict[key] +=1
        else:
            if '(' == strs_list[idx-1]:
                pass
            else:
                sum += pipe_dict.pop(stack_list.pop())
print(sum)
    