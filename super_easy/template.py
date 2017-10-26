import sys


def method(input):
    return ''


if __name__ == '__main__':

    for line in sys.stdin:
        result = method(line)
        if result is not None:
            print(result)
