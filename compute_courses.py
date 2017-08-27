"""
Computes if prereqs are satisfied
TODO:
-Provide a list of class order to take, given some desire to take a course(s).
    e.g. I want to take CS 161, 171, 122B -> take ICS 46, CS 122B, bah
-Provide
"""
def prereq_satisfied(prerequisite, completed):
    for lst in prerequisite:
        if not _at_least_one_satisfied(lst, completed):
            return False

    return True


def _at_least_one_satisfied(course_lst, completed):
    for course in course_lst:
        if course in completed:
            return True

    return False







