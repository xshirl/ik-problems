def findSingleValueTrees(root):

    if root is None:
        return 0
    unival(root)
    return cnt

cnt = 0 
def unival(root):

    global cnt

    if root.right_ptr is None and root.left_ptr is None:
        cnt +=1
        return True

    left, right = True, True

    if root.left_ptr is not None:
        left = unival(root.left_ptr) and root.val == root.left_ptr.val

    if root.right_ptr is not None:
        right = unival(root.right_ptr) and root.val == root.right_ptr.val
        
    if left and right:
        cnt += 1
        
    return left and right