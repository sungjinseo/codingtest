import sys
class MyStack:
    def __init__(self):
        self.stack=[]
        self.i=0
    def set_stack(self,l):
        self.stack=l
        self.i=len(l)
    def get_stack(self):
        return self.stack
    def push(self,x):
        self.stack.append(x)
        self.i+=1
    def pop(self):
        if self.empty():
            return -1
        else:
            tmp=self.top()
            self.stack=self.stack[:-1]
            self.i-=1
            return tmp
    def size(self):
        return self.i
    def empty(self):
        if self.i==0:
            return 1
        else:
            return 0
    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[-1]

class cursor:
    def __init__(self, word):
        self.left_stack=MyStack()
        self.left_stack.set_stack(list(word))
        self.right_stack=MyStack()
    def get_word(self):
        return self.left_stack.get_stack()+list(reversed(self.right_stack.get_stack()))
    def L(self):
        if not self.left_stack.empty():
            self.right_stack.push(self.left_stack.pop())
    def D(self):
        if not self.right_stack.empty():
            self.left_stack.push(self.right_stack.pop())
    def B(self):
        if not self.left_stack.empty():
            self.left_stack.pop()
    def P(self,alp):
        self.left_stack.push(alp)

c= cursor(input())
for _ in range(int(input())):
    command = sys.stdin.readline().strip()
    if command=="L":
        c.L()
    elif command=="D":
        c.D()
    elif command=="B":
        c.B()
    else:
        c.P(command.split()[1])

ans=c.get_word()
print("".join(ans))