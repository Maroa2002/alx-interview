#!/usr/bin/python3
""" 0-stats """
import sys
import signal

file_dict = {}
file_size = 0
line_size = 0
status_code = 0
count = 0

# List of valid status codes
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]


def print_stats():
    """Print statistics"""
    print("File size: {}".format(file_size))
    for k, v in sorted(file_dict.items()):
        print("{}: {}".format(k, v))


def signal_handler(sid, frame):
    """handling keyboard interruption CTRL + C"""
    print_stats()
    sys.exit(0)


# attach the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)


for line in sys.stdin:
    line_split = line.split(" ")

    try:
        status_code = int(line_split[-2])
        line_size = int(line_split[-1])
    except (IndexError, ValueError):
        continue

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
