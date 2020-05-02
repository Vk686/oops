stock_Price = {}
with open("prices.txt", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_Price[day] = price

stock_Price