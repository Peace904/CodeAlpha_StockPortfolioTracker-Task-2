stock_prices = {
    "AMZN": 180,
    "TSLA": 250,
    "AAPL": 170
}
stock = input("Enter stock name (e.g. AAPL): ")
quantity = int(input("Enter quantity: "))
price = stock_prices[stock]
total = price * quantity
print("Total investment:", total)