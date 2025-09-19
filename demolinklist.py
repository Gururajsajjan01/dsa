class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            # First node points to itself
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Display the circular linked list
    def display(self):
        nodes = []
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes) + " -> (back to head)")

    # Delete a node by value
    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return

        curr = self.head

        # Case 1: head node is to be deleted
        if curr.data == key:
            if curr.next == self.head:  # only one node
                self.head = None
                return
            else:
                # Find last node
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = curr.next
                last.next = self.head
                return

        # Case 2: non-head node
        prev = None
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr.data == key:
                prev.next = curr.next
                return

        # Key not found
        print(f"{key} not found in the list")


# -------------------------
# Example Usage
# -------------------------
cll = CircularLinkedList()
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

print("Circular Linked List:")
cll.display()

cll.delete(20)
print("After deleting 20:")
cll.display()
