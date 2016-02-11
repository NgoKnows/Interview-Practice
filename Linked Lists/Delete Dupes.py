import LinkedList

a = LinkedList.LinkedList()

a.append("hii")
a.append("bye")
a.append("hii")
a.append("sup")

def delete_dupes(linked_list):
    values = set()
    cur = linked_list.head
    prev = linked_list.head

    while cur:
        if cur.data not in values:
            values.add(cur.data)
        else:
            prev.next = cur.next
        prev = cur
        cur = cur.next
a.print()
delete_dupes(a)
a.print()




