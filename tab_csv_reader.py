# tab_csv_reader.py
import sys
import csv

try:
    data_file = sys.argv[1]
except:
    print(f"usage: tab_csv_reader.py some_file")
    sys.exit(1)

# files without headers
with open(data_file, 'r') as f:
    tab_reader = csv.reader(f, delimiter='\t')
    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        # process(date, symbol, closing_price)
        print(f"{date}: {symbol} closed in US${closing_price}")
