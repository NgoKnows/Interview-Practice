import LinkedList

a = LinkedList.LinkedList()

a.append(5)
a.append(5)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(1)
a.append(0)


def partition_list(linked_list, partition):
    cur = linked_list.head
    left_partition = []
    right_partition = []
    while cur:
        if cur.data >= partition:
            right_partition.append(cur.data)
        else:
            left_partition.append(cur.data)
        cur = cur.next

    partitioned_list = LinkedList.LinkedList()
    for val in left_partition:
        partitioned_list.append(val)

    for val in right_partition:
        partitioned_list.append(val)

    return partitioned_list

a.print()
p = partition_list(a, 4)
p.print()