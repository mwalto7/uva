import sys


def convert_quotes(text):
    result = []
    if '"' in text:
        count = 0
        for i, char in enumerate(text):
            if char == '"':
                count += 1
                if count % 2 == 0:
                    result.append("''")
                else:
                    result.append("``")
            else:
                result.append(char)
    else:
        result = text

    return ''.join(result)


if __name__ == '__main__':

    text = []
    for line in sys.stdin:
        text.append(line)
    print(convert_quotes(''.join(text)), end='')
