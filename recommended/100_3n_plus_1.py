import sys


def max_cycle_len(start, stop):
    max_cycle = 0
    for num in range(start, stop+1):
        n = num
        cycles = 1
        while n != 1:
            cycles += 1
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = 3*n + 1
        if cycles > max_cycle:
            max_cycle = cycles
    return max_cycle


if __name__ == '__main__':

    for line in sys.stdin:
        line = line.split(' ')
        i = int(line[0])
        j = int(line[1])
        print(i, j, max_cycle_len(i, j))
