class CongaLine:
    """
    An example of a singally linked list.
    """

    class Person:
        """
        Each person in the conga line holds on to the next person in line.
        They do not hold on to the person behind them. They only worry about
        the person in front of them. 
        """

        def __init__(self, name):
            """ 
            Initialize the person to the name provided. Initially
            the person next in line is unknown
            """
            self.name = name
            self.next = None

    def __init__(self):
        """
        Initialize an empty conga line.
        """
        self.head = None
        self.tail = None

    def insert_head(self, name):
        """
        Insert a new person at the front (i.e. the head) of the
        conga line.
        """
        # Create the new node
        new_node = CongaLine.Person(name)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head = new_node      # Update the head 

    def insert_tail(self, name):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        # Create the new node
        new_node = CongaLine.Person(name)

        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # If the list is not empty, then only self.tail will be
        # affected.
        else:
            self.tail.next = new_node # Connect the previous tail to the new node
            self.tail = new_node      # Update the tail to point to the new node

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
            curr_node = self.head
            while curr_node.next != self.tail: # Stop when we have found the node right before the tail
                curr_node = curr_node.next
            assert(curr_node.next == self.tail) # make sure we have found the node right before the tail
            curr_node.next = None  # Disconnect the tail
            self.tail = curr_node  # set the new the tail

    def insert_after(self, name, new_name):
        """
        Insert 'new_value' after the first occurance of 'value' in
        the linked list.
        """
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.name == name:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_name)
                # For any other location of 'value', need to create a 
                # new node and reconenct the links to insert.
                else:
                    new_node = CongaLine.Person(name)
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next = new_node       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'

    def remove(self, name):
        """
        Remove the first node that contains 'value'.
        """
        current_node = self.head
        if current_node.name == name:
            self.remove_head()
            return
        while current_node != None:
            if current_node.next.name == name:
                if current_node.next == self.tail:
                    self.remove_tail()
                    return
                else:
                    current_node.next = current_node.next.next
                    return
            current_node = current_node.next
        
    def replace(self, old_name, new_name):
        """
        Searrch for all instances of 'old_value' and replace the value 
        to 'new_value'.
        """

        current_node = self.head
        while current_node != None:
            if current_node.name == old_name:
                current_node.name = new_name
            current_node = current_node.next

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.name  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

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


###########################################################
# TESTS
###########################################################

# Test 1: conga line has just started and people are joining
line = CongaLine()
line.insert_tail(CongaLine.Person("Terry"))
line.insert_tail(CongaLine.Person("Jerry"))
line.insert_tail(CongaLine.Person("Larry"))
line.insert_tail(CongaLine.Person("Mary"))
print(line)