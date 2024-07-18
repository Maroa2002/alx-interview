#!/usr/bin/python3
""" 0-stats"""
import sys
import re
import signal

file_dict = {}
file_size = 0
line_size = 0
status_code = 0
count = 0

valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - '
    r'\[(?P<date>[^\]]+)\] '
    r'"GET /projects/260 HTTP/1\.1" '
    r'(?P<status_code>\d{3}) '
    r'(?P<size>\d+)'
)


def print_stats():
    """Print statistics"""
    print("File size: {}".format(file_size))
    for k, v in sorted(file_dict.items()):
        print("{}: {}".format(k, v))


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)"""
    print_stats()
    sys.exit(0)


# signal handler for keyboard interruptions
signal.signal(signal.SIGINT, signal_handler)


for line in sys.stdin:
    # line_split = line.strip().split(" ")
    # print(line.strip())
    # status_code = line_split[-2]
    # line_size = int(line_split[-1])
    match = pattern.match(line)
    if match:
        data = match.groupdict()
        status_code = int(data["status_code"])
        line_size = int(data["size"])

        # update the total file size
        file_size += line_size

        if status_code in valid_status_codes:
            if status_code not in file_dict:
                file_dict[status_code] = 1
            else:
                file_dict[status_code] += 1

        count += 1
        if count % 10 == 0:
            print_stats()

print_stats()
