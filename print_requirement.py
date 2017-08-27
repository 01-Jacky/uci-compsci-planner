import downloader
import course
import requirement_parser

course_completed = [
    'I&C SCI 6B',
    'I&C SCI 6D',
    'I&C SCI 6N',
    'I&C SCI 23',
    'I&C SCI 45C',
    'I&C SCI 46',
    'I&C SCI 23',
    'I&C SCI 23',
    'MATH 2A',
    'MATH 2B',
    'STATS 67',
    'COMPSCI 121',
    'COMPSCI 122A',
    'COMPSCI 122B',
    'COMPSCI 132',
    'I&C SCI',
    'COMPUTER SCI & ENGR'
]


def _prereq_satisfied(prerequisite, completed):
    for lst in prerequisite:
        if not _at_least_one_satisfied(lst, completed):
            return False

    return True


def _at_least_one_satisfied(course_lst, completed):
    for course in course_lst:
        if course in completed:
            return True

    return False


def main():
    html = downloader.get_html()
    course_lst = requirement_parser.parse_course(html)

    for course in course_lst:
        print course
        # if not course.graduate:
        #     print "{} - {}".format(course.id, course.title)
        #     for lst in course.prerequisite:
        #         s = " or ".join(lst)
        #         print "  {}".format(s)

    course_not_completed = []
    for course in course_lst:
        if course.id not in course_completed:
            course_not_completed.append(course)

    course_can_take = []
    for course in course_not_completed:
        if not course.graduate and _prereq_satisfied(course.prerequisite, course_completed):
            course_can_take.append(course)

    for course in course_can_take:
        print "{} - {}".format(course.id, course.title)
        # for lst in course.prerequisite:
        #     s = " or ".join(lst)
        #     print "  {}".format(s)

if __name__ == "__main__":
    main()




