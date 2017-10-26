import sys


def minimize_beams(size):
    dimensions = size.split(' ')
    if len(dimensions) < 2:
        return None
    else:
        m = int(dimensions[0])
        n = int(dimensions[1])
        return int(m / 3) * int(n / 3)


if __name__ == '__main__':

    for line in sys.stdin:
        minimum_beams = minimize_beams(line)
        if minimum_beams is not None:
            print(minimum_beams)
