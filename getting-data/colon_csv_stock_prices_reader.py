# tab_csv_reader.py
import sys
import csv

try:
    data_file = sys.argv[1]
except:
    print(f"usage: colon_csv_reader.py some_file")
    sys.exit(1)

# files with headers
with open(data_file, 'r') as f:
    colon_reader = csv.DictReader(f, delimiter=':')
    for dict_row in colon_reader:
        date = dict_row['date']
        symbol = dict_row['symbol']
        closing_price = dict_row['closing_price']
        # process(date, symbol, closing_price)
        print(f"{date}: {symbol} closed in US${closing_price}")
