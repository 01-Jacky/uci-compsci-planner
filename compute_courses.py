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

def get_courses_completed_prereqs(course_lst, completed_lst):
    # Take away course completed
    course_not_completed = [course for course in course_lst if course.id not in inputs.COURSE_COMPLETED]

    # Find classes with prereqs completed
    course_can_take = [course for course in course_not_completed
                       if not course.graduate and compute_courses.prereq_satisfied(course.prerequisite, inputs.COURSE_COMPLETED)]







