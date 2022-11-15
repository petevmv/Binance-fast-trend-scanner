import re
with open('tickers.txt') as file:
	symbols = file.read()
dollar_pair_pattern = '.+USD.*'
dollar_pair = re.findall(dollar_pair_pattern, symbols)
print(dollar_pair)