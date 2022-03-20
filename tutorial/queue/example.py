##########################################################################
# In this example I will walk you through how to implement a priority
# queue for a customer service call center
#
# This call center takes several kinds of calls each with their own
# priority. In order of highest priority to lowest they are:
#       1. Retention (Customers calling to cancel their subscription)
#       2. Customer Service (Customers calling about a problem)
#       3. Sales (Customers calling to place an order)
#
# Follow along with the documentation and inplement this code in the IDE
# and language of your choice! We will run a few tests to see how this
# data structure works.
##########################################################################

class Customer_Service:
    """
    A Customer Service Queue.  Allows new customers to be 
    added and allows customers to be serviced. Takes into account priority.
    """

    class Customer:
        """
        Defines a Customer record for the service queue.
        This is an inner class.  Its real name is CustomerService.Customer
        """

        def __init__(self, name, account_id, problem):
            """
            Initialize the Customer Record

            When a new customer is created, it has a name, account id, 
            and a problem. We will assign the problem a priority. The
            higher the number the higher the priority
            """
            self.name = name
            self.account_id = account_id
            self.problem = problem
            if problem.lower() == "retention":
                self.priority = 4
            elif problem.lower() == "customer service":
                self.priority = 3
            elif problem.lower() == "sales":
                self.priority = 2
            else:
                self.priority = 1

        def __str__(self):
            """
            Return a string representing the record so we can print it out later
            """
            return self.name + " (" + self.account_id + ") : " + self.problem

    def __init__(self, max_size=0):
        """
        Here we will initialize a new customer service queue. It is by default
        empty and contains a max size passed in by the user when it is first
        declared. If no size is passed in or if it is invalid then the default 
        size is 10
        """
        self.queue = []
        if max_size <= 0:
            self.max_size = 10  # Default value if max size is invalid
        else:
            self.max_size = max_size

    def add_new_customer(self):
        """
        Here we will define a function that allows 
        the user to add a new customer to the queue.
        """
        # Verify there is room in the service queue
        if len(self.queue) > self.max_size:
            print("Maximum Number of Customers in Queue.")
            return

        name = input("Customer Name: ")
        account_id = input("Account Id: ")
        problem = input("Problem (Retention, Sales, Customer Service): ")

        # Create the customer object and add it to the queue
        customer = Customer_Service.Customer(name, account_id, problem)
        self.queue.append(customer)

    def serve_customer(self):
        """
        Here we will define a function to serve the next customer.
        Notice we serve based on priority and if there is a tie in 
        priority we serve the customer that was added to the queue 
        first.
        """

        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index
            elif self.queue[index].priority > self.queue[high_pri_index].priority:
                if index < high_pri_index:
                    high_pri_index = index
        # Remove and return the item with the highest priority
        customer = self.queue[high_pri_index]
        self.queue.pop(high_pri_index)
        print(f"Now serving: {customer.name}")

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        customer service queue.  This is useful for debugging.  If you have a 
        Customer_Service object called cs, then you run print(cs) to see the 
        contents.
        """
        result = "[size=" + str(len(self.queue)) + \
            " max_size=" + str(self.max_size) + " => "
        for customer in self.queue:
            # Uses the __str__ from Customer class
            result += "{"+str(customer)+"}"
            result += ", "
        result += "]"
        return result


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
queue = Customer_Service()
queue.add_new_customer()
queue.add_new_customer()
queue.add_new_customer()
queue.add_new_customer()
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
queue = Customer_Service()
queue.add_new_customer()
queue.add_new_customer()
queue.add_new_customer()
print(queue)
queue.serve_customer()
queue.serve_customer()
queue.serve_customer()
