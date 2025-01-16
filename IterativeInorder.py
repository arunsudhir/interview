from collections import deque
class TreeNode():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinaryTree():
    def in_order(self, root):
        node_stack = deque()
        node_stack.append(root)

        while (len(node_stack) > 0):
            while root.left:
                node_stack.append(root.left)
            
            if node_stack:
                curr = node_stack.pop()
                print(curr.val)
            
            if curr.right:
                node_stack.append(curr.right)

def main():
    root = TreeNode(1)
    l1_left = TreeNode(2)
    l1_right = TreeNode(3)
    l2_left1 = TreeNode(4)
    l2_left2 = TreeNode(5)
    l2_right1 = TreeNode(6)
    l2_right2 = TreeNode(7)
    root.left = l1_left
    root.right = l1_right
    l1_left.left = l2_left1
    l1_left.right = l2_left2
    l1_right.left = l2_right1
    l1_right.right = l2_right2

    BinaryTree().in_order(root)



