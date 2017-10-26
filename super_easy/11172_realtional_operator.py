import sys


def find_relation(values):
    values = values.split(' ')
    if len(values) > 1:
        a = int(values[0])
        b = int(values[1])
        if a < b:
            return '<'
        if a > b:
            return '>'
        if a == b:
            return '='
    else:
        return None


if __name__ == '__main__':

    for line in sys.stdin:
        result = find_relation(line)
        if result is not None:
            print(result)
