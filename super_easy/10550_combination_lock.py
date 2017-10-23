import sys


def calculate_degrees(combination):
    nums = []
    count = 0
    for num in combination.split(' '):
        count += int(num)
        nums.append(int(num))

    if count == 0:
        return None
    else:
        total = 1080

        if nums[0] - nums[1] < 0:
            total += 9 * (40 + nums[0] - nums[1])
        else:
            total += 9 * (nums[0] - nums[1])

        if nums[2] - nums[1] < 0:
            total += 9 * (40 + nums[2] - nums[1])
        else:
            total += 9 * (nums[2] - nums[1])

        if nums[2] - nums[3] < 0:
            total += 9 * (40 + nums[2] - nums[3])
        else:
            total += 9 * (nums[2] - nums[3])

        return total


if __name__ == '__main__':

    for line in sys.stdin:
        total_degrees = calculate_degrees(line)
        if total_degrees is not None:
            print(total_degrees)




