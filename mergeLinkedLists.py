'''
    class SinglyLinkedListNode:
        def __init__(self, node_data):
            self.data = node_data
            self.next = None

    The function accepts an ARRAY of SinglyLinkedListNodes as input 
    and is expected to return a SinglyLinkedListNode.

    Complete the function below.
'''

def merge_k_lists(lists):
    nodes = []
    head = ll = SinglyLinkedListNode(0)
    for list in lists:
        while list:
            nodes.append(list.data)
            list = list.next
    for node in sorted(nodes):
        ll.next = SinglyLinkedListNode(node)
        ll = ll.next
    return head.next 