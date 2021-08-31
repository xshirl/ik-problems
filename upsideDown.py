def upsideDown(root):
  if not root:
        return None
        
    s = []
    while root:
        #print(root.val)
        s.append(root)
        root= root.left_ptr
    
    root = cur = s.pop()
    while s:
        cur.left_ptr = s[-1].right_ptr
        cur.right_ptr = s.pop()
        cur = cur.right_ptr
        cur.right_ptr = None
        cur.left_ptr = None
        
    return root