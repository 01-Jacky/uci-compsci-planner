import sys
import compute_courses
import downloader
import inputs
import requirement_parser
import compute_courses

def main():
    # Get fall requirements
    html = downloader.get_courses_html()
    course_lst = requirement_parser.parse_course(html)
    courses_can_take = compute_courses.get_courses_completed_prereqs(course_lst)
    courses_can_take_fall_17 = compute_courses.get_courses_can_take_quarter(courses_can_take, inputs.COURSE_COMPLETED ,inputs.FALL_CS_COURSE_ID)

    print '{:*^50}'.format("Course you completed ")
    for course_id in inputs.COURSE_COMPLETED:
        print "  {}".format(course_id)
    print ""

    print '{:*^50}'.format(" All CS upper div with prereqs cleared ")
    for course in courses_can_take:
        print "  {} - {}".format(course.id, course.title)
    print ""

    print '{:*^50}'.format(" CS upper div you can take in Fall 2017 ")
    for course in courses_can_take_fall_17:
        print "  {} - {}".format(course.id, course.title)
        # for lst in course.prerequisite:
        #     s = " or ".join(lst)
        #     print "  {}".format(s)
    print ""


if __name__ == "__main__":
    main()