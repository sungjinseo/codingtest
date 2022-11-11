
if __name__ == '__main__':
    deque_size = 100000
    head, tail = int(deque_size/2), int(deque_size/2)+1
    deque = [-1 for _ in range(100000)]
    
    input_cnt = input()
    input_cnt = int(input_cnt)
    cmd_list = []
    
    for i in range(input_cnt):
        cmd_list.append(input().split(' '))
    
    for cmd in cmd_list:
        
        if 'push_front' == cmd[0]:
            deque[head] = cmd[1]
            head -= 1
            
        elif 'push_back' == cmd[0]:
            deque[tail] = cmd[1]
            
            
        elif 'pop_front' == cmd[0]:
            if head == tail-1:
                print(-1)
            else:
                print(deque[head+1])
                head +=1
            
        elif 'pop_back' == cmd[0]:
            if head == tail-1:
                print(-1)
            else:  
                print(deque[tail-1])
                tail -=1
        
        elif 'size' == cmd[0]:
            print(tail - head)
            
        elif 'empty' == cmd[0]:
            if head == tail-1:
                print(1)
            else:
                print(0)
            
        elif 'front' == cmd[0]:
            if head == tail-1:
                print(-1)
            else:
                print(deque[head+1])
        
        elif 'back' == cmd[0]:
            if head == tail-1:
                print(-1)
            else:
                print(deque[tail-1])
