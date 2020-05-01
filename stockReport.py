import json


def write_json(data, filename):
    with open(filename, 'w') as addStock:
        json.dump(data, addStock, indent=4)


def stock(element):  # Return True if passed Element is Present else return False
    with open('stock.json') as stockReport:
        dataOnFile = json.load(stockReport)
        for datas in dataOnFile["reportDetail"]:
            if datas.get("stockName") == element:
                return True
    return False


def add():  # To add New Entry into the JSON File

    stockName = input("Enter Your Stock Nmae: ")
    stockNumber = str(input("Enter Your Stock Number: "))
    stockPrice = str(input("Enter Your Stock Price: "))
    try:
        stockDetail = {
            "stockName": stockName,
            "stockNumber": stockNumber,
            "stockPrice": stockPrice
           
        }
        with open('stock.json') as stockReport:
            dataOnFile = json.load(stockReport)
            temp = dataOnFile["reportDetail"]
            temp.append(stockDetail)
        write_json(dataOnFile, 'stock.json')
        print("Data Saved !!!")
    except:
        stockDetail = {
            "reportDetail": [
                {
                    "stockName": stockName,
                    "stockNumber": stockNumber,
                    "stockPrice": stockPrice,
                   
                   }
            ]}
        write_json(stockDetail, 'stock.json')
        print("Data Saved !!!")


def search(element):  # Search for Data Based on FirstName or MobileNumber or LastName of the Entry

    with open('stock.json') as stockReport:
        dataOnFile = json.load(stockReport)
    for datas in dataOnFile["reportDetail"]:
        if element == datas.get("stockName") or element == datas.get("stockNumber") or element == datas.get("stockPrice"):
            print(datas)


search("VEDANTA")
add()            