"""
Problem Description:
You want to keep track of which students come to 
class and how often they come. You need a way to sort 
them because they don't all walk into class by alphabetical 
order and don't all come every day since attendance is optional 
except for the final exam where everyone must come to class. 
Implement a BST to solve this problem.
"""

class SemesterAttendance_BST:

    class Student:
        
        def __init__(self, name):
            pass


    def __init__(self):
        pass

    def insert(self, name):
        pass

    def _insert(self, name, current_student):
        pass

    def __contains__(self, name):
        pass

    def _contains(self, name, current_student):
        pass

    def __iter__(self):
        pass
        
    def _traverse_forward(self, current_student):
        pass
        
    def __reversed__(self):      
        pass

    def _traverse_backward(self, current_student):
        pass

    def get_height(self):
        pass

    def _get_height(self, current_student):
        pass

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

