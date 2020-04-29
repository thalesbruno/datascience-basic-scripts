# email_domain_count.py
import sys
from collections import Counter

try:
    data_file = sys.argv[1]
except:
    print(f"usage: email_domain_count.py somefile")
    sys.exit(1)


def get_domain(email_address: str) -> str:
    """ Split on '@' and return the last piece"""
    return email_address.split('@')[-1]


with open(data_file, 'r') as f:
    counter = Counter(get_domain(line.strip())
                      for line in f
                      if '@' in line)


print(dict(counter))
