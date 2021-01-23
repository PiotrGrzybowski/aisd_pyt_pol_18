from structures.lists import LinkedList, Node


def is_cycle_in_list(values: LinkedList) -> bool:
    if values.head is None:
        return False
    else:
        visited = [values.head]
        pointer = values.head
        while pointer.next is not None and pointer.next not in visited:
            pointer = pointer.next
            visited.append(pointer)

        return pointer.next is not None


if __name__ == '__main__':
    node_1 = Node(3)
    node_2 = Node(2)
    node_3 = Node(0)
    node_4 = Node(-4)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    node_4.next = node_2

    values = LinkedList()
    values.head = node_1

    print(is_cycle_in_list(values))

