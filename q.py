class q:
    def __init__(self):
        self.li = []

    def insert(self, val):
        self.li.append(val)

    def delete(self):
        temp = self.li.pop(0)
        return temp
    
    def isEmpty(self):
        if not self.li:
            return True
        return False
    
    def peek(self):
        return self.li[0]
    
    def show(self):
        print(self.li)
    
que = q()
que.insert(1)
que.insert(2)
que.insert(3)
que.insert(4)
que.insert(5)

que.show()

print(que.delete())
print(que.delete())
print(que.delete())

que.show()

print(que.isEmpty())

