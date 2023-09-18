class Node:
    def __init__(self, data):
        self.data= data #data는 값을 가리키는 변수(속성, attribute)
        self.next= None #next는 다음 노드를 가리키는 변수

class Linked_list:
    def __init__(self):
        self.head= None
        self.length= 0
    
    def __len__(self):
        return self.length
        
    def append_left(self, data):
        node = Node(data)
        if self.head is None:
            self.head= node
        else:
            node.next= self.head
            self.head= node
        self.length +=1

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head= node
        else:
            prev= self.head
            while prev.next:
                prev= prev.next
            prev.next= node
        self.length += 1
        
    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            node= self.head
            while node.next: #node.next is not None
                print(node.data, end = " → ")
                node= node.next
            print(node.data)
            
    def search(self, data):
        node= self.head
        while node:
            if node.data == data:
                return True
            node= node.next
        return False
        
    def pop_left(self):
        if self.heaed is None:
            return None
        node= self.head
        self.head= self.headn.next
        self.length -= 1
        return node.data
        
    def pop(self):
        if self.head is None:
            return None
        node= self.head
        if self.head.next is None:
            self.head = None
        else:
            while node.next is not None:
                prev= node
                node= node.next
            prev.next= None
        self.length -=1
        return node.data
        
    def insert(self, index, data):
        if index <= 0:
            self.append_left(data)
        elif index >= self.lenght:
            self.append(data)
        else:
            prev= self.head
            for _ in range(i-1):
                prev= prev.next
            node= Node(data)
            node.next= prev.next
            prev.next= node
            self.length += 1
            
    def remove(self, data):
        if self.head.data == data:
            self.popleft()
            return True
        prev = self.head
        while prev.next:
            if prev.next.data == data:
                prev.next = prev.next.next
                self.length -= 1
                return True
            prev = prev.next
        return False
        
    def is_there_loop(_list):
        node1 = node2 = _list.head
        while node1 and node1.next:
            node1 = node1.next.next #첫째 노드는 두 칸씩 이동
            node2 = node2.next      #둘째 노드는 한 칸씩 이동
            if node1 == node2:
                return True
        return False
        
    def reverse(self):
        if self.length <= 1:
            return
        ahead = self.head.next
        prev = self.head
        prev.next = None
        while ahead:
            self.head = ahead
            ahead = ahead.next
            self.head.next = prev
            prev = self.head
        
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = node.next
        return node.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.front is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        node = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return node.data

    def is_empty(self):
        return self.front is None

class Hash_table:
    def __init__(self, length = 5):
        self.max_len = length
        self.table = [[] for _ in range(self.max_len)]

    def hash(self, key):
        res = sum([ord(s) for s in key])
        return res % self.max_len

    def set(self, key, value): #해시 테이블에 key와 value를 넣는다.
        index = self.hash(key)
        self.table[index].append((key, value))

    def get(self, key):      #해시 테이블에서 key의 value를 찾는다.
        index = self.hash(key)
        value = self.table[index]
        if not value:         #찾는 키가 없으면 None을 반환
            return None
        for v in value:       #리스트에서 값을 찾아 반환 
            if v[0] == key:
                return v[1]
        return None

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node=None):
        self.root = node
        
    def preorder(self):
        def _preorder(node):
            if node is None:
                return
            res.append(node.data)
            _preorder(node.left)
            _preorder(node.right)

        res = []
        _preorder(self.root)
        return res

    def inorder(self):
        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            res.append(node.data)
            _inorder(node.right)

        res = []
        _inorder(self.root)
        return res

    def postorder(self):
        def _postorder(node):
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            res.append(node.data)

        res = []
        _postorder(self.root)
        return res
        
    def levelorder(self):
        res = []
        if not self.root:
            return res
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            res.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def insert_key(self, key):
        new_node = TreeNode(key)
        if not self.root:
            self.root = new_node
        else:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                if node.left is None:
                    node.left = new_node
                    break
                else:
                    queue.append(node.left)
                if node.right is None:
                    node.right = new_node
                    break
                else:
                    queue.append(node.right)
                    
    def delete_key(self, key):
        q = [(self.root, self.root)]
        delete_node = None
        while q:
            node, last_parent = q.pop(0)
            last_node_data = node.data
            if node.data == key:
                delete_node = node
            if node.left:
                q.append((node.left, node))
            if node.right:
                q.append((node.right, node))
    
        if delete_node is None:
            print(f"There is not {key}")
        else:
            delete_node.data = last_node_data
            if last_parent.right is not None:
                last_parent.right = None
            else:
                last_parent.left = None
                
    def find_has_no_sibling(self):
        res, q = [], [self.root]
        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)            
                if not node.right:
                    res.append(node.left.data)
                    continue
            if node.right:
                q.append(node.right)
                if not node.left:
                    res.append(node.right.data)
                    continue
    
        return res if res else [-1]
        
    def make_tree(self, arr):
        if not arr:
            return
        self.root = TreeNode(arr[0])
        q = [self.root]
        index = 1
        while q and index < len(arr):
            node = q.pop(0)
            if index < len(arr) and arr[index] is not None:
                node.left = TreeNode(arr[index])
                q.append(node.left)
            index += 1
            if index < len(arr) and arr[index] is not None:
                node.right = TreeNode(arr[index])
                q.append(node.right)
            index += 1