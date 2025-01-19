import sys

def convert(line):
    if line[0] == 'S':
        if line[2] == 'M':
            line = line[4:-2]
            result = ''
            for char in line:
                if char.isupper():
                    result += f' {char.lower()}'
                else:
                    result += char
            print(result)
        elif line[2] in {'V', 'C'}:
            line = line[4:]
            result = ''
            for char in line:
                if char.isupper():
                    result += f' {char.lower()}'
                else:
                    result += char
            print(result.strip())
    elif line[0] == 'C':
        if line[2] == 'M':
            line = line[4:]
            words = line.split()
            result = words[0]
            for word in words[1:]:
                result += word.capitalize()
            print(result + '()')
        elif line[2] == 'C':
            line = line[4:]
            words = line.split()
            result = ''
            for word in words:
                result += word.capitalize()
            print(result)
        elif line[2] == 'V':
            line = line[4:]
            words = line.split()
            result = words[0]
            for word in words[1:]:
                result += word.capitalize()
            print(result)

if __name__ == '__main__':
    entry = sys.stdin.read()
    lines = entry.splitlines()
    for line in lines:
        convert(line)
