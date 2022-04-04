class SemesterAttendance_BST:
    """
    One of many possible solutions to implementing an
    attendance sheet for a single semester.
    """

    class Student:
        """
        Each student has a name and an attendance for the semester
        """

        def __init__(self, name):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.name = name
            self.attendance = 1
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, name):
        """
        Insert the student by name into the BST. 
        If the student has never come to class, add them to the tree.
        """
        if self.root is None:
            self.root = SemesterAttendance_BST.Student(name)
        else:
            self._insert(name, self.root)  # Start at the root

    def _insert(self, name, current_student):
        """
        This function will look for a place to insert a student
        with 'name' and 'attendance' inside of it.  
        The current sub-tree is represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        # If the student is already in the tree don't reinsert them, 
        # just add one to their attendance.
        if name == current_student.name:
            current_student.attendance += 1
            return

        if name < current_student.name:
            # The data belongs on the left side.
            if current_student.left is None:
                # We found an empty spot
                current_student.left = SemesterAttendance_BST.Student(name)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(name, current_student.left)
        else:
            # The data belongs on the right side.
            if current_student.right is None:
                # We found an empty spot
                current_student.right = SemesterAttendance_BST.Student(name)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(name, current_student.right)

    def __contains__(self, name):
        """ 
        Checks if name is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(name, self.root)  # Start at the root

    def _contains(self, name, current_student):
        """
        This funciton will search for a student with the name 'name'
        The current sub-tree being search is 
        represented by 'current_student'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if name == current_student.name:
            return True
        if name < current_student.name:
            # The data would be on the left side
            if current_student.left is None:
                # It is not in the list
                return False
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                return self._contains(name, current_student.left)
        else:
            # The data would be on the right side.
            if current_student.right is None:
                # It is not in the list
                return False
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                return self._contains(name, current_student.right)

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, current_student):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if current_student is not None:
            yield from self._traverse_forward(current_student.left)
            yield f'{current_student.name} - {current_student.attendance} attendances'
            yield from self._traverse_forward(current_student.right)
        
    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, current_student):
        """
        Does a backwards traversal (reverse in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by 
        the __reversed__ function.        
        """
        if current_student is not None:
            yield from self._traverse_backward(current_student.right)
            yield current_student.name
            yield from self._traverse_backward(current_student.left)

    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, current_student):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.

        Notice here that the stopping condition for the recursive call 
        is when there is no node connected to the previous node. 
        We know that if this is the case then we are at the end of the 
        tree and we will not add another to our height count hence why 
        we return 0.
        """
        if current_student is None:
            return 0
        else:
            return 1 + max(self._get_height(current_student.left),  self._get_height(current_student.right))

# NOTE: Functions below are not part of the BST class above. 

def create_bst_from_sorted_list(sorted_list):
    """
    Given a sorted list (sorted_list), create a balanced BST.  If 
    the values in the sorted_list were inserted in order from left
    to right into the BST, then it would resemble a linked list (unbalanced). 
    To get a balanced BST, the _insert_middle function is called to 
    find the middle item in the list to add first to the BST.  The 
    _insert_middle function takes the whole list but also takes a 
    range (first to last) to consider.  For the first call, the full 
    range of 0 to len()-1 used.
    """
    bst = SemesterAttendance_BST()  # Create an empty BST to start with 
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst

def _insert_middle(sorted_list, first, last, bst):
    """
    This function will attempt to insert the item in the middle
    of 'sorted_list' into the 'bst' tree.  The middle is 
    determined by using indicies represented by 'first' and 'last'.
    For example, if the function was called on:

    sorted_list = [10, 20, 30, 40, 50, 60]
    first = 0
    last = 5

    then the value 30 (index 2 which is the middle) would be added 
    to the 'bst' (the insert function above can be used to do this).   

    Subsequent recursive calls are made to insert the middle from the values 
    before 30 and the values after 30.  If done correctly, the order
    in which values are added (which results in a balanced bst) will be:

    30, 10, 20, 50, 40, 60

    This function is intended to be called the first time by 
    create_bst_from_sorted_list.

    The purpose for having the first and last parameters is so that we do 
    not need to create new sublists when we make recursive calls.  Avoid 
    using list slicing to create sublists to solve this problem.

    """
    if len(sorted_list) == 0:
        return
        
    if first + 1 == last or last - 1 == first:
        bst.insert(sorted_list[first])
        bst.insert(sorted_list[last])

    elif first == last:
        bst.insert(sorted_list[first])

    else:
        middle = (first + last) // 2
        bst.insert(sorted_list[middle])
        _insert_middle(sorted_list, first, middle - 1, bst)
        _insert_middle(sorted_list, middle + 1, last, bst)


##########################################################
# TEST CASES
##########################################################

# The first day of class the following students walk in: 
# Edgar, Sam, Samuel, Dominic, Fred, Beth, Bethany, April
# Expected Output: 
# April - 1 attendances
# Beth - 1 attendances
# Bethany - 1 attendances
# Dominic - 1 attendances
# Edgar - 1 attendances
# Fred - 1 attendances
# Sam - 1 attendances
# Samuel - 1 attendances
roster = SemesterAttendance_BST()
print("ATTENDANCE ON THE FIRST DAY OF SCHOOL")
roster.insert("Edgar")
roster.insert("Sam")
roster.insert("Samuel")
roster.insert("Dominic")
roster.insert("Fred")
roster.insert("Beth")
roster.insert("Bethany")
roster.insert("April")
for student in roster:
    print(student)
print()

# The next day of class the following students walk in: 
# Samuel, Dominic, Fred, Beth, Eddie
# Expected Output: 
# April - 1 attendances
# Beth - 2 attendances
# Bethany - 1 attendances
# Dominic - 2 attendances
# Eddie - 1 attendances
# Edgar - 1 attendances
# Fred - 2 attendances
# Sam - 1 attendances
# Samuel - 2 attendances
print("ATTENDANCE ON THE SECOND DAY OF SCHOOL")
roster.insert("Samuel")
roster.insert("Dominic")
roster.insert("Fred")
roster.insert("Beth")
roster.insert("Eddie")
for student in roster:
    print(student)
print()

# The last day of class is the exam date. Everyone must come to class
# The following students walk in: 
# Edgar, Sam, Samuel, Dominic, Fred, Beth, Bethany, April, Eddie, Kyle, Kelly, Kaleb, Caleb, Roger, Becky
# Expected Output: 
# April - 2 attendances
# Becky - 1 attendances
# Beth - 3 attendances
# Bethany - 2 attendances
# Caleb - 1 attendances
# Dominic - 3 attendances
# Eddie - 2 attendances
# Edgar - 2 attendances
# Fred - 3 attendances
# Kaleb - 1 attendances
# Kelly - 1 attendances
# Kyle - 1 attendances
# Roger - 1 attendances
# Sam - 2 attendances
# Samuel - 3 attendances

print("ATTENDANCE ON THE LAST DAY OF SCHOOL")
roster.insert("Edgar")
roster.insert("Sam")
roster.insert("Samuel")
roster.insert("Dominic")
roster.insert("Fred")
roster.insert("Beth")
roster.insert("Bethany")
roster.insert("April")
roster.insert("Eddie")
roster.insert("Kyle")
roster.insert("Kelly")
roster.insert("Kaleb")
roster.insert("Caleb")
roster.insert("Roger")
roster.insert("Becky")
for student in roster:
    print(student)
print()

