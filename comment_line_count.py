# comment_line_count.py
import sys
import re

try:
    data_file = sys.argv[1]
except:
    print(f"usage: comment_line_count.py some_file")
    sys.exit(1)

starts_with_hash = 0

with open(data_file, 'r') as f:
    for line in f:
        if re.match("^#", line.strip()):
            starts_with_hash += 1

print(f"number of comment lines: {starts_with_hash}")
