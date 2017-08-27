""" Data model for a Course """
import re

class Course:
    def __init__(self, id, title, prerequisite=[]):
        self.id = id
        self.title = title
        self.prerequisite = prerequisite
        self.graduate = self._is_graduate(self.id)

    def __repr__(self):
        return "{}:{}".format(self.id, self.__dict__)

    def _is_graduate(self, id):
        pattern = re.compile(".+2\d\d")
        if pattern.match(id):
            return True
        else:
            return False

if __name__ == "__main__":
    c = Course('COMPSCI 213', 'someclass')
    print c.graduate


