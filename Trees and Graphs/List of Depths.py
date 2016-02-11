from collections import dequeue

def list_depths(root, queue=None, levels=None, index=0):
    if queue is None:
        queue = dequeue([root])
    if levels is None:
        levels = dict()

    levels[index] = LinkedList()
queue2 = dequeue()
while len(queue1):
    node = queue.pop()
    levels[index].add(node)
    if node.left:
        queue2.append(node.left)
    if node.right:
        queue2.append(node.right)
return list_depths(root, queue, levels, index + 1)






