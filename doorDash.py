import locale


def main() -> None:
    locale.setlocale(locale.LC_ALL, "")
    recipients = int(input("Number of recipiants: "))
    theDict = {}

    # Loop through the number of people and get their names
    # Empty input will skip that person (For myself usually. I don't need to know my own total)
    for i in range(recipients):
        name = input(f"Name for person {i + 1}: ")
        if name == "":
            pass
        else:
            stopLoop = False
            items = 0
            while not stopLoop:
                # Keep accepting a person's items. If input is empty this assumes that you are done with that person.
                item = input("Enter item costs: ")
                if not item:
                    stopLoop = True
                    theDict[name] = items
                    pass
                else:
                    item = float(item)
                    items += item

    fees = float(input("Doordash fees: "))
    tax = float(input("Taxes: "))
    tip = float(input("Tip: "))

    # Add fees to each person's total and show the output
    print("===========================")
    for key in theDict:
        theDict[key] += float(fees / recipients)
        theDict[key] += float(tax / recipients)
        theDict[key] += float(tip / recipients)
        print(f"{key}: {locale.currency(theDict[key], grouping=True)}")
    print("===========================")


if __name__ == "__main__":
    main()
