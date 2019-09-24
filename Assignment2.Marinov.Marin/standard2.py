# Define the data structure
dataSet = [
    {"f1": "high", "f2": "vhigh", "f3": 3, "f4": 4,
        "f5": "medium", "f6": "high", "iClass": 'Q'},
    {"f1": "high", "f2": "medium", "f3": 4, "f4": 6,
        "f5": "small", "f6": "high", "iClass": 'S'},
    {"f1": "medium", "f2": "vhigh", "f3": 3, "f4": 1,
        "f5": "big", "f6": "medium", "iClass": 'S'},
    {"f1": "medium", "f2": "high", "f3": 3, "f4": 4,
        "f5": "big", "f6": "high", "iClass": 'R'},
    {"f1": "low", "f2": "high", "f3": 4, "f4": 4,
        "f5": "small", "f6": "low", "iClass": 'S'},
    {"f1": "low", "f2": "vhigh", "f3": 3, "f4": 1,
        "f5": "big", "f6": "medium", "iClass": 'Q'},
    {"f1": "low", "f2": "vhigh", "f3": 1, "f4": 6,
        "f5": "small", "f6": "high", "iClass": 'P'},
    {"f1": "low", "f2": "high", "f3": 3, "f4": 1,
        "f5": "medium", "f6": "low", "iClass": 'S'},
    {"f1": "low", "f2": "low", "f3": 4, "f4": 6,
        "f5": "small", "f6": "medium", "iClass": 'Q'},
    {"f1": "vlow", "f2": "low", "f3": 3, "f4": 1,
        "f5": "big", "f6": "low", "iClass": 'P'},
    {"f1": "vlow", "f2": "low", "f3": 6, "f4": 4,
        "f5": "small", "f6": "high", "iClass": 'S'},
    {"f1": "vlow", "f2": "low", "f3": 4, "f4": 4,
        "f5": "big", "f6": "medium", "iClass": 'R'}
]

#####################
# Functions
#####################


def getFilteredSpace(dataset, className):
    filteredArr = []
    for item in dataSet:
        for value in item.values():
            if (value == className):
                filteredArr.append(item)
    return filteredArr


def printFilteredSpace(space):
    for instance in space:
        print("\n")
        print(instance)


def analyzef1(data):
    highs = 0
    mediums = 0
    lows = 0
    vlows = 0

    for item in data:
        for key, value in item.items():
            if (key == 'f1'):
                if (value == "high"):
                    highs += 1
                elif (value == "medium"):
                    mediums += 1
                elif (value == "low"):
                    lows += 1
                elif (value == "vlow"):
                    vlows += 1

    return {"highCount": highs, "mediumsCount": mediums, "lowsCount": lows, "vlowCount": vlows}


def analyzef2(data):
    vhighs = 0
    highs = 0
    medium = 0
    lows = 0

    for item in data:
        for key, value in item.items():
            if (key == 'f1'):
                if (value == "vhigh"):
                    vhighs += 1
                elif (value == "high"):
                    highs += 1
                elif (value == "medium"):
                    medium += 1
                elif (value == "low"):
                    lows += 1

    return {"vhighCount": vhighs, "highsCount": highs, "lowsCount": lows, "mediumCount": medium}


def analyzef3(data):
    threeCount = 0
    fourCount = 0
    oneCount = 0

    for item in data:
        for key, value in item.items():
            if (key == "f3"):
                if (value == 4):
                    fourCount += 1
                elif (value == 3):
                    threeCount += 1
                elif (value == 1):
                    oneCount += 1

    return {"4": fourCount, "3": threeCount, "1": oneCount}


def analyzef4(data):
    sixCount = 0
    fourCount = 0
    oneCount = 0

    for item in data:
        for key, value in item.items():
            if (key == "f4"):
                if (value == 6):
                    sixCount += 1
                elif (value == 4):
                    fourCount += 1
                elif (value == 1):
                    oneCount += 1

    return {"6": sixCount, "4": fourCount, "1": oneCount}


def analyzef5(data):
    bigs = 0
    mediums = 0
    smalls = 0

    for item in data:
        for key, value in item.items():
            if (key == "f5"):
                if (value == "big"):
                    bigs += 1
                elif (value == "medium"):
                    mediums += 1
                elif (value == "small"):
                    smalls += 1

    return {"big": bigs, "medium": mediums, "small": smalls}


def analyzef6(data):
    bigs = 0
    mediums = 0
    smalls = 0

    for item in data:
        for key, value in item.items():
            if (key == "f6"):
                if (value == "big"):
                    bigs += 1
                elif (value == "medium"):
                    mediums += 1
                elif (value == "small"):
                    smalls += 1

    return {"big": bigs, "medium": mediums, "small": smalls}

#####################
# Output
#####################


filteredQ = getFilteredSpace(dataSet, 'Q')
filteredR = getFilteredSpace(dataSet, 'R')
filteredS = getFilteredSpace(dataSet, 'S')
filteredP = getFilteredSpace(dataSet, 'P')


print("Classification Q: ")
printFilteredSpace(filteredQ)
print("\n")
print(analyzef1(filteredQ).items())
print(analyzef2(filteredQ))
print(analyzef3(filteredQ))
print(analyzef4(filteredQ))
print(analyzef5(filteredQ))
print(analyzef6(filteredQ))
print("\nClassification R: ")
printFilteredSpace(filteredR)
print("\n")
print(analyzef1(filteredR))
print(analyzef2(filteredR))
print(analyzef3(filteredR))
print(analyzef4(filteredR))
print(analyzef5(filteredR))
print(analyzef6(filteredR))
print("\nClassification S: ")
printFilteredSpace(filteredS)
print("\n")
print(analyzef1(filteredS))
print(analyzef2(filteredS))
print(analyzef3(filteredS))
print(analyzef4(filteredS))
print(analyzef5(filteredS))
print(analyzef6(filteredS))
print("\nClassification P: ")
printFilteredSpace(filteredP)
print("\n")
print(analyzef1(filteredP))
print(analyzef2(filteredP))
print(analyzef3(filteredP))
print(analyzef4(filteredP))
print(analyzef5(filteredP))
print(analyzef6(filteredP))
