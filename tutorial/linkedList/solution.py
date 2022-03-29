class CustomerServiceQueue:
    """
    A customer service priority queue implemented as a double linked list
    """

    class Customer:
        """
        Each node of the linked list will have data and links to the 
        previous and next node. 
        """

        def __init__(self, name, problem=""):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.name = name
            if problem.lower() == "retention":
                self.priority = 4
            elif problem.lower() == "customer service":
                self.priority = 3
            elif problem.lower() == "sales":
                self.priority = 2
            else:
                self.priority = 1
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def add_new_customer(self, name, problem=""):
        """
        Add a new customer to the priority queue
        """
        if self.head == None:
            self.head = CustomerServiceQueue.Customer(name, problem)
            self.tail = self.head
        else:
            new_customer = CustomerServiceQueue.Customer(name, problem)
            self.tail.next = new_customer
            new_customer.prev = self.tail
            self.tail = new_customer
    
    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node
        
    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.tail
        # will be affected.
        elif self.tail is not None:
            self.tail.prev.next = None  # Disconnect the second node from the first node
            self.tail = self.tail.prev  # Update the head to point to the second node

    def serve_customer(self):
        """
        Serve the customer with the highest priority. 
        If there is a tie, serve the customer that was there the first.
        """
        highest_priority = self.head
        node = self.head
        while node is not None:
            if node.priority > highest_priority.priority:
                highest_priority = node
            node = node.next
        if highest_priority == self.head:
            self.remove_head()
        elif highest_priority == self.tail:
            self.remove_tail()
        else:
            highest_priority.prev.next = highest_priority.next
            highest_priority.next.prev = highest_priority.prev
        print(f"Now serving: {highest_priority.name}")

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.name  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    def __reversed__(self):
        """
        Iterate backward through the Linked List
        """
        current_node = self.tail
        while current_node is not None:
            yield current_node.data
            current_node = current_node.prev

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output


##########################################################################
# TESTS
#
# Now we will run a few tests to make sure that this queue works as
# expected and to exercise it's power.
##########################################################################

# TEST 1: Testing simple priority
# Input: (Bob, 1, Sales) (Sue, 2, Retention) (Jake, 3, Other) (Dom, 4, Customer Service)
# Expected Result: Sue, Dom, Bob, Jake
print("Test 1")
queue = CustomerServiceQueue()
queue.add_new_customer("Bob", "Sales")
queue.add_new_customer("Sue", "Retention")
queue.add_new_customer("Jake", "Other")
queue.add_new_customer("Dom", "Customer Service")
print(queue)
queue.serve_customer()
queue.serve_customer()
queue.serve_customer()
queue.serve_customer()
print(queue)

# Test 2: Testing simple tie
# Input: (Bob, 1, sales) (Sue, 2, Retention) (Jake, 3, Retention)
# Expected Result: Sue, Jake, Bob
print("Test 2")
queue = CustomerServiceQueue()
queue.add_new_customer("Bob", "Sales")
queue.add_new_customer("Sue", "Retention")
queue.add_new_customer("Jake", "Retention")
print(queue)
queue.serve_customer()
queue.serve_customer()
queue.serve_customer()
