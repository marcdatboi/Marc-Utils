



# Imports
import Node


# ---=== Linked List Class ===---
class LinkedList:
    def __init__(self, head) -> None:
        self.head = Node(head)
        self.tail = self.head


    # === Append To Head Method ===
    def append_head(self, new_data):
        new_node = Node(new_data)

        # Check if head is empty :)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node


    # === Append to Tail Method ===
    def append_tail(self, new_data):
        new_node = Node(new_data)

        # Check if tail is empty
        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node


    # === Remove Node ===
    # Removes from either the head node or tail node
    def remove(self, specifier: str = "h"): # specifier = h, specifier = t
        match specifier.lower():

            case "h": # Remove from the head node
                if self.head is None:
                    print("No Head or Tail to Remove!")
                    return

                # This checks if the head OR tail is the only value remaining
                elif self.head.get_next() is None:
                    self.head = None
                    self.tail = None
                    print("Linked List is NOW Empty!")

                else: # If there's multiple values in the L.L.
                    self.head = self.head.get_next()
                    self.head.set_prev(None)
                    print("Head successfully removed!")

            case "t":
                if self.tail is None:
                    print("No Head or Tail to Remove!")
                    return

                elif self.tail.get_next() is None:
                    self.tail = None
                    self.head = None
                    print("Linked List is NOW Empty!")

                else:
                    self.tail = self.tail.get_prev()
                    self.tail.set_next(None)
                    print("Tail successfully removed!")


    # === Remove by value (search) ===
    def remove_value(self, value_to_search_for):
        if self.head is None:
            print("Linked List is empty!")

        elif self.head.get_next() is None:
            self.head = None
            print("Linked List is Now Empty!")

        else:
            # Check if the head OR tail values is what we need.
            if self.head.get_data() == value_to_search_for:
                self.remove("h")

            elif self.tail.get_data() == value_to_search_for:
                self.remove("t")

            else: # Look through all the nodes in the linked list
                current_node = self.head
                while current_node.next() is not None:
                    if current_node.get_data() == value_to_search_for:
                        current_node.get_prev().set_next \
                            (current_node.get_next()) # Set the previous node's next pointer to current.next
                        current_node.get_next().set_prev \
                            (current_node.get_prev()) # Set the next nodes prev pointer to current.prev
                        current_node = None
                        print("Value removed sucessfully!")
                        return
                    else:
                        current_node = current_node.get_next()
                print("Could not find value")
                return


    # === Display Linked List ===
    def display(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        else:
            print("<head> ", end="")
            current_node = self.head
            while current_node is not None:
                print(f"{current_node.get_data()} -> ", end="")
                current_node = current_node.get_next()
            print("<tail>")


    # === Clear entire LL method ===
    def clear(self):
        self.head = None
        self.tail = None

        # --- Helpers ---
    def is_head_none(self): # This can also work for checking if the tail is 'None'
        return self.head is None