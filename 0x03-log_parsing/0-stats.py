#!/usr/bin/python3
""" Log parsing """
import sys


def print_stats(total_size, status_codes):
    """ Print statistics """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))


def parse_line(line):
    """ Parse a line from the log """
    try:
        parts = line.split()
        size = int(parts[-1])
        code = int(parts[-2])
        return (size, code)
    except (ValueError, IndexError):
        return (0, 0)


def main():
    """ Main function """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            size, code = parse_line(line)
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
            count += 1

            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
