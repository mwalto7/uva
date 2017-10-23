import sys


if __name__ == '__main__':

    text = []
    for line in sys.stdin:
        text.append(line)

    print(''.join(text), end='')
