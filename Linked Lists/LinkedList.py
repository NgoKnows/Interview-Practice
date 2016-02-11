class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def delete(self, index):
        cur = self.head
        prev = self.head
        i = 0

        if index == 0:
            self.head = self.head.next

        while i != index and cur:
            prev = cur
            cur = cur.next
            i += 1

        if i == index:
            prev.next = cur.next

    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
        print('\n')