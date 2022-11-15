import sys
from tradingview_ta import *
import colorama
from colorama import Fore

def red_green_neutral(analis):
	# print(analis.summary['RECOMMENDATION'])
	if analis is None:
		return '' 
		
	elif analis.summary['RECOMMENDATION'] in ["SELL", 'STRONG_SELL']:
		print (Fore.RED + analis.symbol, analis.summary['RECOMMENDATION'])
	elif analis.summary['RECOMMENDATION'] in ['BUY', 'STRONG_BUY']:
		print (Fore.GREEN + analis.symbol, analis.summary['RECOMMENDATION'])
	
	else:	
		print (Fore.CYAN + analis.symbol, analis.summary['RECOMMENDATION'])

def analysis(symbols):
	result = get_multiple_analysis(screener='Crypto',
								 interval=Interval.INTERVAL_5_MINUTES,
								 symbols=symbols)
	return result

all_binance_pairs = 'tickers.txt'
only_usd_pairs = 'binance_dollar_pairs.txt'

with open(all_binance_pairs) as file:
	symbols = eval(file.read())

if len(sys.argv) > 1:
	searced_list = []
	for symbol in symbols:
		if str(sys.argv[1]) in str(symbol):
			searced_list.append(symbol)
	analysis = analysis(searced_list)
	for symbol in searced_list:
		# print(searced_list)
		red_green_neutral(analysis[symbol])

else:
	analysis = analysis(symbols)
	for symbol in symbols:
		red_green_neutral(analysis[symbol])
# handler = TA_Handler(symbol = ["BTCBUSD", "SOLBUSD", "ETHBUSD"],
# 					screener = 'Crypto',
# 					exchange = 'Binance',
# 					interval = Interval.INTERVAL_5_MINUTES)

# handler2 = TA_Handler(symbol = "SOLBUSD",
# 					screener = 'Crypto',
# 					exchange = 'Binance',
# 					interval = Interval.INTERVAL_5_MINUTES)

# handler3 = TA_Handler(symbol = "ETHBUSD",
# 					screener = 'Crypto',
# 					exchange = 'Binance',
# 					interval = Interval.INTERVAL_5_MINUTES)





# print('BTCBUSD', handler.get_analysis().summary)
# print('SOLBUSD', handler2.get_analysis().summary)
# print('ETHBUSD', handler3.get_analysis().summary)


# color = Fore.RED if handler.get_analysis().summary['RECOMMENDATION'] == 'SELL' else Fore.GREEN
# print(color + 'BTCUSD', handler.get_analysis().summary)
# color = Fore.RED if handler2.get_analysis().summary['RECOMMENDATION'] == 'SELL' else Fore.GREEN
# print(color + 'SOLBUSD', handler2.get_analysis().summary)
# color = Fore.RED if handler3.get_analysis().summary['RECOMMENDATION'] == 'SELL' else Fore.GREEN
# print(color + 'ETHBUSD', handler3.get_analysis().summary)

# working
# red_green_neutral(handler.get_analysis())
# red_green_neutral(handler2.get_analysis())
# red_green_neutral(handler3.get_analysis())


# for symbol in symbols:
# 	red_green_neutral(analysis[symbol])
	
# print(sys.argv[1:])
# print(analysis['BINANCE:BTCBUSD'].summary)
# print(red_green_neutral(analysis))