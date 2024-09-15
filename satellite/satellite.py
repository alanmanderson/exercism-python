def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder): raise ValueError("Array lengths don't match")
    if len(preorder) != len(set(preorder)): raise ValueError("Array contains duplicates")
    if len(inorder) != len(set(inorder)): raise ValueError("Array contains duplicates")
    return tree_from_traversals_helper(preorder,inorder)

def tree_from_traversals_helper(preorder,inorder):
    if len(preorder) == 0:
        return {}
    root = preorder.pop(0)
    idx = inorder.index(root)
    left = inorder[0: idx]
    preorder_left = preorder[0:len(left)] 
    right = inorder[idx+1: len(inorder)]
    preorder_right = preorder[len(left):]
    return {
            "v":root, 
            "l": tree_from_traversals_helper(preorder_left, left), 
            "r": tree_from_traversals_helper(preorder_right, right)
    }
