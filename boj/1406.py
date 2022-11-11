class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

if __name__ == '__main__':
    
    input_str = input()
    input_num = input()
    input_num = int(input_num)
    
    cur_list = ['' for i in range(input_num)]
    
    for idx in range(len(cur_list)):
        cur_list[idx] = input()
    
    head = ListNode(-1)
    cur = ListNode('')
    
    head.next = cur
    cur.prev = head
    
    for ss in list(input_str):
        tmp_node = ListNode(ss)
        tmp_node.prev = cur.prev
        tmp_node.next = cur
        cur.prev.next = tmp_node
        cur.prev = tmp_node
    
    for cmd in cur_list:
        ch = cmd.split(' ')

        if 'L' == ch[0]:
            prev = cur.prev
            next = cur.next
            
            if prev.prev != None:
                prev.prev.next = cur
                cur.next = prev
                cur.prev = prev.prev
                prev.next = next
        
        elif 'D' == ch[0]:
            prev = cur.prev
            next = cur.next
            
            if next != None:
                prev.next = next
                cur.next = next.next
                cur.prev = next
                next.next = cur
            
        elif 'B' == ch[0]:
            prev = cur.prev
            
            if prev.prev != None:
                prev.prev.next = cur
                cur.prev = prev.prev
                
            
        elif 'P' == ch[0]:
            tmp_node = ListNode(ch[1])
            prev = cur.prev
            tmp_node.prev = prev
            tmp_node.next = cur
            cur.prev.next = tmp_node
            cur.prev = tmp_node
    
    node = head
    while node:
        if node.val != -1 and node.val != '':
            print(node.val, end='')
        node = node.next