class node(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def inorder(self, root):
        ans = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            ans.append(root.val)
            helper(root.right)
        helper(root)
        return ans

    def prorder(self, root):
        ans = []
        def helper(root):
            if not root:
                return
            ans.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return ans

    def postorder(self, root):
        ans = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            ans.append(root.val)
        helper(root)
        return ans
    
root = node(4)
root.left = node(2)
root.right = node(6)
root.left.left = node(1)
root.left.right = node(3)
root.right.left = node(5)
root.right.right = node(7)

print("Inorder Traversal :", root.inorder(root))
print("Preorder Traversal :", root.prorder(root))
print("Postorder Traversal :", root.postorder(root))