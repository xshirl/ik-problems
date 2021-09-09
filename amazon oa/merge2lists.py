def merge(l1, l2):
  curr = ll = Node(0)
  while l1 and l2:
    if l1.val < l2.val:
      curr.next = l1
      l1 = l1.next
    else:
      curr.next = l2
      l2 = l2.next
    curr = curr.next
  return ll.next
  