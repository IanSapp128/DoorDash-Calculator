import locale


def main() -> None:
    locale.setlocale(locale.LC_ALL, "")
    recipients = int(input("Number of parties: "))
    individuals = 0
    theDict = {}
    theDict2 = {}

    # Loop through the number of people and get their names
    # Empty input will skip that person (For myself usually. I don't need to know my own total)
    for i in range(recipients):
        name = input(f"Name for party {i + 1}: ")
        if name == "":
            pass
        else:
            people = input(f"How many people in this party?")
            theDict2[name] = int(people)
            individuals += int(people)
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

    regFees = float(input("Regulatory fee: "))
    deliveryFee = float(input("Delivery fee: "))
    serviceFee = float(input("Service fee: "))
    tax = float(input("Taxes: "))
    tip = float(input("Tip: "))

    # Add fees to each person's total and show the output
    print("=========Totals=========")
    for key in theDict:
        theDict[key] += float((regFees / individuals) * theDict2[key])
        theDict[key] += float((deliveryFee / individuals) * theDict2[key])
        theDict[key] += float((serviceFee / individuals) * theDict2[key])
        theDict[key] += float((tax / individuals) * theDict2[key])
        theDict[key] += float((tip / individuals) * theDict2[key])
        print(f"{key}: {locale.currency(theDict[key], grouping=True)}")
    print("========================")


if __name__ == "__main__":
    main()
