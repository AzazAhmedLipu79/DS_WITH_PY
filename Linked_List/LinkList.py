class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(f'Data is {self.data} & Next is {self.next}')


print(Node())


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def __repr__(self) -> str:
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(current_node)
            current_node = current_node.next

        return nodes
