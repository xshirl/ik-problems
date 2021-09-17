
"""
    For your reference:
    class SinglyLinkedListNode:
        def __init__(self, node_data):
            self.data = node_data
            self.next = None

    class TreeNode():
        def __init__(self, val=None, left_ptr=None, right_ptr=None):
            self.val = val
            self.left_ptr = left_ptr
            self.right_ptr = right_ptr

    Complete the function below.
"""


def sorted_list_to_bst(head):
    """
        Args:
         head(SinglyLinkedListNode_int32)
        Returns:
         TreeNode_in32
    """
    root = helper(head)
    return root
    
def helper(node):
    if node is None:
        return
    if node.next is None:
        return TreeNode(node.data)
    slow = node
    fast = node
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next


    prev.next = None
    mid = slow
    root_node = TreeNode(mid.data)
    root_node.left_ptr = helper(node)
    root_node.right_ptr = helper(mid.next)
    
    return root_node
