
class Taking_Turns_Queue:
    """
    This queue is circular.  When people are added via add_person, then they are added to the 
    back of the queue (per FIFO rules).  When get_next_person is called, the next person
    in the queue is displayed and then they are placed back into the back of the queue.  Thus,
    each person stays in the queue and is given turns.  When a person is added to the queue, 
    a turns parameter is provided to identify how many turns they will be given.  If the turns is 0 or
    less than they will stay in the queue forever.  If a person is out of turns then they will 
    not be added back into the queue.
    """

    class Person:
        """
        A person is defined with a name and a number of turns.
        """

        def __init__(self, name, turns):
            """
            Initialize the person
            """
            self.name = name
            if turns == 0:
                self.turns = -1
            else:
                self.turns = turns

        def __str__(self):
            """
            Support the display of single person.
            """
            if self.turns <= 0:
                result = "({}:Forever)".format(self.name)
            else:
                result = "({}:{})".format(self.name, self.turns)
            return result

    def __init__(self):
        """ 
        Start with an empty queue
        """
        self.people = Queue()

    def add_person(self, name, turns):
        """
        Add new people to the queue with a name and number of turns
        """
        person = Taking_Turns_Queue.Person(name, turns)
        self.people.enqueue(person)

    def get_next_person(self):
        """
        Get the next person in the queue and display them.  The person should
        go to the back of the queue again unless the turns variable shows that they 
        have no more turns left.  Note that a turns value of 0 or less means the 
        person has an infinite number of turns.  An error message is displayed 
        if the queue is empty.
        """
        if self.people.is_empty():
            print("No one in the queue.")
        else:
            person = self.people.dequeue()
            if person.turns > 1:
                person.turns -= 1
                self.people.enqueue(person)
            elif person.turns < 0:
                self.people.enqueue(person)
            print(person.name)

    def __len__(self):
        """
        Support the len() function
        """
        return len(self.people)

    def __str__(self):
        """
        Provide a string representation of everyone in the queue
        """
        return str(self.people)
