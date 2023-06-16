from typing import Optional


class Node:
    def __init__(self, value: str, next: Optional["Node"] = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail = self.head

    def add_node(self, node: Node) -> None:
        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        self.tail = curr
        self.tail.next = node
        self.tail = node

    def __repr__(self) -> str:
        result = ""
        curr = self.head
        while curr:
            result += f"{curr.value} -> {curr.next.value if curr.next else None}\n"
            curr = curr.next
        return result

    def count_nodes(self) -> int:
        curr = self.head
        count: int = 1
        while curr.next:
            count += 1
            curr = curr.next
        return count

    def remove(self, index: int) -> int:
        start: int = 0
        curr = self.head
        if not index and curr.next is None:
            self.head = None
            return 0

        while curr.next:
            if not index:
                self.head = curr.next
                return 0
            if start == index - 1:
                curr.next = curr.next.next
                return 0
            start += 1
            curr = curr.next
        return -1


nodeA = Node("red")
nodeB = Node("Green")
nodeC = Node("Blue")
nodeD = Node("Yellow")
nodeE = Node("Pink")
linked_list = LinkedList()
linked_list.add_node(nodeA)
linked_list.add_node(nodeB)
linked_list.add_node(nodeC)
linked_list.add_node(nodeD)
linked_list.add_node(nodeE)

print(linked_list)
print(linked_list.count_nodes())
linked_list.remove(4)
print(linked_list)
linked_list.remove(2)
print(linked_list)
