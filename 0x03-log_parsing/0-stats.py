#!/usr/bin/python3
""" 0-stats"""
import sys
import re
import signal

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

file_dict = {}
file_size = 0
line_size = 0
status_code = 0
count = 0

valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
pattern = r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - \[(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)'


for line in sys.stdin:
    # line_split = line.strip().split(" ")
    # print(line.strip())
    # status_code = line_split[-2]
    # line_size = int(line_split[-1])
    match = re.match(pattern, line.strip())
    if match:
        status_code = int(match.group("status"))
        line_size = int(match.group("size"))

        file_size += line_size

        if status_code in valid_status_codes:
            if status_code not in file_dict:
                file_dict[status_code] = 1
            else:
                file_dict[status_code] += 1

        count += 1
        if count % 10 == 0:
            print("File size: {}".format(file_size))
            for k, v in sorted(file_dict.items()):
                print("{}: {}".format(k, v))
