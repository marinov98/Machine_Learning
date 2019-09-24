# Define the data structure
InstanceSpace = [
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


def getFilteredSpace(dictionary, className):
    filteredArr = []
    for item in dictionary:
        for value in item.values():
            if (value == className):
                filteredArr.append(item)
    return filteredArr


def printFilteredSpace(space):
    for instance in space:
        print("\n")
        print(instance)


filteredQ = getFilteredSpace(InstanceSpace, 'Q')
filteredR = getFilteredSpace(InstanceSpace, 'R')
filteredS = getFilteredSpace(InstanceSpace, 'S')
filteredP = getFilteredSpace(InstanceSpace, 'P')

print("Classification Q: ")
printFilteredSpace(filteredQ)
print("\nClassification R: ")
printFilteredSpace(filteredR)
print("\nClassification S: ")
printFilteredSpace(filteredS)
print("\nClassification P: ")
printFilteredSpace(filteredP)
