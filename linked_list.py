from node import Node


class LinkedList:

    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    def insert_node(self, data):
        # Create a new node with the given data
        new_node = Node(data)

        # Case 1: The linked list is empty
        if self._head is None:
            self._head = new_node

        # Case 2: The new data is less than or equal to the current head data
        elif data <= self._head.data:
            new_node.next_node = self._head
            self._head = new_node

        # Case 3: Inserting in the middle or at the end of the list
        else:
            previous = self._head
            runner = self._head.next_node
            while runner is not None and data > runner.data:  # https://imgur.com/a/xOjYmNm
                previous = runner
                runner = runner.next_node
            new_node.next_node = runner  # https://imgur.com/a/4UVuIJO
            previous.next_node = new_node  # https://imgur.com/a/CE7P7IG
        # PS : the imgur link's purpose is to better understand and visualize what happens when inserting a new node.

        # Example:
        # 1. Insert a node with the value 9
        """Iteration 1: Executed when checking whether the linked list is empty.
        Linked List: 9
        """
        # 2. Insert a node with the value 3
        """Iteration 2: Executed when data <= self._head.data
        Linked List: 3 -> 9
        """
        # 3. Insert a node with the value 7
        """Iteration 3: Executed when data > self._head_data BUT data < self.head_data.next_node
        Linked List: 3 -> 7 -> 9
        """
        # 4. Insert a node with the value 15
        """Iteration 4: Executed when data > self._head_data AND data > self.head_data.next_node
        Linked List: 3 -> 7 -> 9 -> 15

        ADDITIONAL INFO
        It basically reaches that last node in the list which is the TAIL. It creates a new node, creates the connection
        between the OLD TAIL and the NEW TAIL(The new node that has the value '15').
        """

    def print_linked_list(self):
        if self._head is None:
            print("Linked list is empty")
            return  # Exit the function
        current = self._head
        count = 0
        while current is not None:
            if count > 0:
                print(f" -> {current.data}", end="")
            else:
                print(current.data, end="")
            current = current.next_node
            count += 1

    def count_nodes(self):
        return self.count_nodes_recursive(self._head)

    def count_nodes_recursive(self, node):  # node = self._head in this case
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes_recursive(node.next_node)

    def find_node(self, target_data):
        current = self._head
        while current is not None:  # https://imgur.com/a/YJhd1ej (NOT FOUND YET TARGET)
            if current.data == target_data:
                return True  # https://imgur.com/a/qXR155C (FOUND)
            current = current.next_node

        return False  # https://imgur.com/a/tS0ZfFy (NOT FOUND)

    def delete_node(self, target_data):
        # Case 1: The linked list is empty
        if self._head is None:
            return False

        # Case 2: The node to be deleted is the head
        elif self._head.data == target_data:
            self._head = self._head.next_node  # https://imgur.com/a/y6f5ryQ
            return True

        # Case 3: The node to be deleted is in the middle or at the end
        else:
            previous = self._head
            runner = self._head.next_node  # the node that will be deleted

            while runner is not None and target_data > runner.data:  # https://imgur.com/a/9gRChPe
                previous = runner          # 2nd; 3rd; 4th
                                           #  ↓    ↓    ↓
                runner = runner.next_node  # 3rd; 4th; 5th

            if runner is not None and target_data == runner.data:
                previous.next_node = runner.next_node  # Bridge
                return True
            return False

