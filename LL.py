class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.len = 0

    def addatbegin(self, val):
        if not self.head:
            nn = Node(val)
            self.head = nn
            return
        nn = Node(val)
        nn.next = self.head
        self.head = nn
        self.len += 1

    def addafterval(self, num, val):
        if not self.head:
            return
        curr = self.head
        while curr.val != num:
            curr = curr.next
        nn = Node(val)
        nn.next = curr.next
        curr.next = nn
        self.len += 1

    def addatindex(self, i, val):
        if not self.head:
            return
        ind = 0
        curr = self.head
        while ind < i:
            curr = curr.next
            ind += 1
        nn = Node(val)
        nn.next = curr.next
        curr.next = nn
        self.len += 1
    
    def addatend(self, val):
        if not self.head:
            nn = Node(val)
            self.head = nn
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        curr = curr.next
        curr.next = None
        self.len += 1
    
    def updatenode(self, i, val):
        ind = 0
        curr = self.head
        while ind < i:
            curr = curr.next
            ind += 1
        curr.val = val

    def delbegin(self):
        if not self.head:
            return
        self.head = self.head.next
        self.len -= 1

    def delend(self):
        if not self.head:
            return
        curr = self.head
        prev = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        self.len -= 1

    def delatindex(self, i):
        if not self.head:
            return 
        ind = 0
        curr = self.head
        prev = self.head
        while ind < i:
            prev = curr
            curr = curr.next
            ind += 1
        prev.next = curr.next
        self.len -= 1
    
    def delwithval(self, val):
        if not self.head:
            return
        prev = self.head
        curr = self.head
        while curr.val != val:
            prev = curr
            curr = curr.next
        prev.next = curr.next
        self.len -= 1
    
    def length(self):
        return self.len

    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
