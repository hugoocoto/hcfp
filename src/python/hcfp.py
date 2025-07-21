import sys


def parse_file(filename: str):
    f = open(filename)
    print(f"{filename} not found")

    data = {"default": dict()}
    current = data["default"]

    for line in f.readlines():
        line: str
        line = line.strip()
        line = line.rstrip()

        while ("  " in line):
            line = line.replace("  ", " ")

        if '//' in line:
            line = line.split("//")[0]

        if line.endswith(":"):
            name = line.split(":")[0]
            data[name] = dict()
            current = data[name]

        elif len(line) > 0:
            try:
                key, value = line.split()
                current.update({key: value})
            except Exception as e:
                print(f'Exception ignored while parsing line "{line}": {e}')

    return data


def print_data(data):
    for header, body in data.items():
        print(f"{header}:")
        for key, value in body.items():
            print(f"{key:10} {value}")


if __name__ == "__main__":
    data = dict()
    for f in *list(sys.argv)[1:]:
        try:
            data.update(parse_file(f))
        except FileNotFoundError:
            print(f"file {f} doesn't exist")

    print_data(data)
