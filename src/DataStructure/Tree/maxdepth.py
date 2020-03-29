#iterative

def maxDepth(self, root: TreeNode) -> int:
    stack, max_depth = [(root, 1)], 0
    while stack and root:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        if node.right: stack.append((node.right, depth + 1))
        if node.left: stack.append((node.left, depth + 1))
    return max_depth


#recursive

def maxDepth(self, root: TreeNode) -> int:
        return self.depthFunc(root, 0)

    def depthFunc(self, root, depth):
        if root:
            return max(self.depthFunc(root.left, depth), self.depthFunc(root.right, depth)) + 1
        return 0