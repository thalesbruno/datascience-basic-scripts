# egrep.py
#
# This script reads text from stdin (line by line)
# and spits back out the lines that match a regular expression

import re
import sys

# sys.argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at the command line
regex = sys.argv[1]

# for every line passed into script
for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)
