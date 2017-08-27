import sys
import compute_courses
import downloader
import inputs
import requirement_parser



def main(args=None):
    html = downloader.get_html()
    course_lst = requirement_parser.parse_course(html)

    # for course in course_lst:
    #     print course

    # Take away course completed
    course_not_completed = [course for course in course_lst if course.id not in inputs.COURSE_COMPLETED]

    # Find classes with prereqs completed
    course_can_take = [course for course in course_not_completed
                       if not course.graduate and compute_courses.prereq_satisfied(course.prerequisite, inputs.COURSE_COMPLETED)]

    print "*** Based on the course you completed *** "
    for course_id in inputs.COURSE_COMPLETED:
        print "  {}".format(course_id)
    print ""

    print "*** CS upper div you can take ***"
    for course in course_can_take:
        print "  {} - {}".format(course.id, course.title)
    print ""

    print "*** CS upper div you can take in Fall 2017 ***"
    for course in course_can_take:
        if course.id in inputs.FALL_CS_COURSE_ID:
            print "  {} - {}".format(course.id, course.title)
            # for lst in course.prerequisite:
            #     s = " or ".join(lst)
            #     print "  {}".format(s)
    print ""


if __name__ == "__main__":
    main()