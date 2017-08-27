from bs4 import BeautifulSoup
import itertools
import course as c


def parse_course(html):
    course_list = []
    soup = BeautifulSoup(html, 'html.parser')

    table_course = soup.find_all('table')[5]

    for tr in table_course.findAll('tr')[1:]:

        td = tr.findAll('td')[0]
        if len(td.findAll('a')) == 0:
            continue
        if len(td.findAll('a')) == 1:
            course_id = _get_single_space(td.text)
        else:
            course_id = _get_single_space(td.findAll('a')[1].text)           # 2nd anchor link is the right one

        course_title = _get_single_space(tr.findAll('td')[1].text)
        prereq_list = _get_prereq_list(tr.findAll('td')[2])

        # print course_id + " " + course_title
        course_list.append(c.Course(course_id, course_title, prereq_list))

    return course_list


def _get_single_space(s):
    """ Returns a string with extra spaces removed. e.g. CS     111 -> CS 111"""
    return ' '.join(s.split())


def _get_prereq_list(el):
    lst = []
    for c in el.contents:
        s = str(c).strip().replace(';','')

        if '<b>' in s:
            continue
        if s == '':
            continue
        s = _get_single_space(s)
        lst.append(s)
        lst = [k for k, g in itertools.groupby(lst)]      # Remove duplicate <br>

    prereq_list = [[]]
    i = 0
    for s in lst:
        if s != '<br/>':
            prereq_list[i].append(s)
        else:
            prereq_list.append([])
            i += 1

    return prereq_list

