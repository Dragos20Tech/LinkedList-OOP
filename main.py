from linked_list import LinkedList

linked_list = LinkedList()

linked_list.insert_node(9)
linked_list.insert_node(3)
linked_list.insert_node(7)
linked_list.insert_node(15)

print("BEFORE DELETING:")
linked_list.print_linked_list()

# Count the number of nodes in the linked list
print(f"\nNumber of nodes in the linked list: {linked_list.count_nodes()} nodes")

# Delete the 3rd node in the list
linked_list.delete_node(9)
print("\nAFTER DELETING:")
linked_list.print_linked_list()

# Count the number of nodes in the linked list
print(f"\nNumber of nodes in the linked list: {linked_list.count_nodes()} nodes")

# Find a node in the linked list
print(f"\nIs the node with the value 9 in the list?")
print(linked_list.find_node(9))


print(f"\nIs the node with the value 7 in the list?")
print(linked_list.find_node(7))
