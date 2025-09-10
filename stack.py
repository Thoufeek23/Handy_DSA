class stack:
    def __init__(self):
        self.li = []
    def push(self, val):
        self.li.append(val)
    def pop(self):
        temp = self.li.pop()
        return temp
    def peek(self):
        return self.li[-1]
    def isEmpty(self):
        if not self.li:
            return True
        return False
    def show(self):
        print(self.li)
    
s = stack()
s.push(2)
s.push(3)
s.push(4)
s.show()
print(s.pop())
print(s.peek())
s.push(8)
s.show()
print(s.isEmpty())