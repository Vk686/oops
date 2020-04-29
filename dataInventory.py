import json


def write_json(data, filename):
    with open(filename, 'w') as addBook:
        json.dump(data, addBook, indent=4)


def elementExists(element):  # Return True if passed Element is Present else return False
    with open('book.json') as addressBook:
        dataOnFile = json.load(addressBook)
        for datas in dataOnFile["personalDetail"]:
            if datas.get("firstname") == element:
                return True
    return False


def add():  # To add New Entry into the JSON File

    firstName = input("Enter Your First_Name: ")
    lastName = input("Enter Your Last_Name: ")
    address = input("Enter Your Address: ")
    city = input("Enter Your CITY: ")
    state = input("Enter Your State: ")
    zip = str(input("Enter your ZIP Number: "))
    phoneNumber = str(input("Enter your Phone Number: "))
    try:
        addressDetail = {
            "firstname": firstName,
            "lastName": lastName,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip,
            "phoneNumber": phoneNumber
        }
        with open('book.json') as addressBook:
            dataOnFile = json.load(addressBook)
            temp = dataOnFile["personalDetail"]
            temp.append(addressDetail)
        write_json(dataOnFile, 'book.json')
        print("Data Saved !!!")
    except:
        addressDetail = {
            "personalDetail": [
                {
                    "firstname": firstName,
                    "lastName": lastName,
                    "address": address,
                    "city": city,
                    "state": state,
                    "zip": zip,
                    "phoneNumber": phoneNumber}
            ]}
        write_json(addressDetail, 'book.json')
        print("Data Saved !!!")


def search(element):  # Search for Data Based on FirstName or MobileNumber or LastName of the Entry

    with open('book.json') as addressBook:
        dataOnFile = json.load(addressBook)
    for datas in dataOnFile["personalDetail"]:
        if element == datas.get("firstname") or element == datas.get("phoneNumber") or element == datas.get("lastName"):
            print(datas)


def delete(element):  # Delete a Object from JSON file based on FirstName

    if elementExists(element) == False:
        print("Data Not Present")
        return None
    with open('book.json') as addressBook:
        dataOnFile = json.load(addressBook)
    temp = []
    for datas in dataOnFile["personalDetail"]:
        if element == datas.get("firstname"):
            pass
        else:
            temp.append(datas)
    dictionary = {"personalDetail": temp}
    write_json(dictionary, 'book.json')
    print("Data Deleted")


search("Vishwas")
add()
