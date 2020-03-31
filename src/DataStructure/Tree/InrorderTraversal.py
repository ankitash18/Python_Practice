def inordertraversal(root):
    if not root:
        return  []
    arr =[]
    inorder(root,arr)
    return arr


def inorder(self,root,arr):
        if not root :
            return
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)

#def inorderTraversal(self, root):
  #      return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []


  #iteratvie soluton-

  def inorder(root):
      ans =[]
      stack =[]
      while stack or root:
          if root:
              stack.append(root)
              root = root.left
          else:
              tmpnode = stack.pop()
              ans.append(tmpnode.val)
              root = tmpnode.right

      return ans