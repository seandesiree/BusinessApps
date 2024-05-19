stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]

def stock_analyser(stock_data):
    stock_data = stock_data[0], stock_data[1], stock_data[2]
    symbol = input("What ticker symbol do you want to analyze? ").upper()

    total = ""
    total = [data[2] for data in stock_data if data[0].upper() == symbol]
    
    if total:
        avg = sum(total) / len(total)
        print(f"The average price for {symbol} is {avg} ")
    else:
        print(f"No data found for {symbol}. ")
        
stock_analyser(stock_data)


