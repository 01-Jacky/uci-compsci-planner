"""
Computes if prereqs are satisfied
TODO:
-Provide a list of class order to take, given some desire to take a course(s).
    e.g. I want to take CS 161, 171, 122B -> take ICS 46, CS 122B, bah
-Provide
"""
import inputs


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


def get_courses_completed_prereqs(course_lst):
    # Take away course completed
    course_not_completed = [course for course in course_lst if course.id not in inputs.COURSE_COMPLETED]
    # Find classes with prereqs completed
    courses_can_take = [course for course in course_not_completed
                       if not course.graduate and prereq_satisfied(course.prerequisite, inputs.COURSE_COMPLETED)]

    return courses_can_take


def get_courses_can_take_quarter(courses_can_take, course_completed, course_offered):
    ans = []
    for course in courses_can_take:
        if course.id in course_offered and course.id not in course_completed:
            ans.append(course)

    return ans



