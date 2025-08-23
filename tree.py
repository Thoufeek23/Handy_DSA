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
    
    def bfs(self, root):
        if not root:
            return
        
        queue = [root]
        result = []

        while queue:
            level = []
            next_queue = []

            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            
            result.append(level)
            queue = next_queue
        
        return result

    
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
print("BFS :", root.bfs(root))