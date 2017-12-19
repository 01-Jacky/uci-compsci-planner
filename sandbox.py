import re

def _is_graduate(id):
    pattern = re.compile(".+2\d\d")
    if pattern.match(id):
        return True
    else:
        return False

print _is_graduate('COMPSCI 123')
print _is_graduate('COMPSCI 2')
print _is_graduate('COMPSCI 23')
print _is_graduate('COMPSCI 223')

