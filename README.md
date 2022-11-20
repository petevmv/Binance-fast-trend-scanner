# How to use the scanner
Make sure you have all the files in same directory.

`binance_dollar_pais.txt` file contains all $ pairs and are represented in `scanner.py` as `only_usd_pairs`

`tickers.txt` file contains all available ticker symbols from binance and are represented in `scanner.py` as `all_binance_pairs`

open `scanner.py` with text editor and find the following line of code 

`with open(all_binance_pairs) as file:`

and replace it one of the two choises above. (`only_usd_pairs` or `all_binance_pairs`)
    
    


First make sure you have all python-packages already installed using terminal and type
`pip install tradingview-ta colorama`

If we want to scan all of the provided data we just type in terminal `python scanner.py`

If we want to be specific about trading pair or just in general a specic crypto we type in terminal for example `python scanner.py LTC` and the output will be trading pairs with LTC only