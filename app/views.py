from flask import render_template
from app import app
from engine import downloader
from engine import requirement_parser
from engine import compute_courses
from engine import inputs
import requests

@app.route('/')
@app.route('/index')
def index():
    html = downloader.get_courses_html()                    # Get fall requirements
    course_lst = requirement_parser.parse_course(html)
    courses_can_take = compute_courses.get_courses_completed_prereqs(course_lst)
    courses_can_take_fall_17 = compute_courses.get_courses_can_take_quarter(courses_can_take, inputs.COURSE_COMPLETED ,inputs.FALL_CS_COURSE_ID)

    return render_template(
        "index.html",
        title='Home',
        courses_can_take = courses_can_take,
        courses_can_take_fall_17 = courses_can_take_fall_17,
        )