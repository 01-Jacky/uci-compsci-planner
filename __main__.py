import sys
import compute_courses
import downloader
import inputs
import requirement_parser


def get_courses_can_take(course_lst):
    # Take away course completed
    course_not_completed = [course for course in course_lst if course.id not in inputs.COURSE_COMPLETED]
    # Find classes with prereqs completed
    courses_can_take = [course for course in course_not_completed
                       if not course.graduate and compute_courses.prereq_satisfied(course.prerequisite, inputs.COURSE_COMPLETED)]

    return courses_can_take


def main():
    # Get fall requirements
    html = downloader.get_courses_html()
    course_lst = requirement_parser.parse_course(html)
    courses_can_take = get_courses_can_take(course_lst)

    print '{:*^50}'.format(" Based on the course you completed ")
    for course_id in inputs.COURSE_COMPLETED:
        print "  {}".format(course_id)
    print ""

    print '{:*^50}'.format(" All CS upper div with prereqs cleared ")
    for course in courses_can_take:
        print "  {} - {}".format(course.id, course.title)
    print ""

    print '{:*^50}'.format(" CS upper div you can take in Fall 2017 ")
    for course in courses_can_take:
        if course.id in inputs.FALL_CS_COURSE_ID:
            print "  {} - {}".format(course.id, course.title)
            # for lst in course.prerequisite:
            #     s = " or ".join(lst)
            #     print "  {}".format(s)
    print ""


if __name__ == "__main__":
    main()