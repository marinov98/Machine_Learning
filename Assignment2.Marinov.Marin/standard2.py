from math import log
from scipy.stats import entropy

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


def analyzef1(dataset):
    dataf1 = {"high": [], "medium": [], "low": [], "vlow": []}

    for item in dataset:
        if (item["f1"] == "high"):
            dataf1["high"].append(item["iClass"])
        elif (item["f1"] == "medium"):
            dataf1["medium"].append(item["iClass"])
        elif (item["f1"] == "low"):
            dataf1["low"].append(item["iClass"])
        elif (item["f1"] == "vlow"):
            dataf1["vlow"].append(item["iClass"])

    return dataf1


def analyzef2(dataset):
    dataf2 = {"vhigh": [], "high": [], "medium": [], "low": []}

    for item in dataset:
        if (item["f2"] == "vhigh"):
            dataf2["vhigh"].append(item["iClass"])
        elif (item["f2"] == "high"):
            dataf2["high"].append(item["iClass"])
        elif (item["f2"] == "medium"):
            dataf2["medium"].append(item["iClass"])
        elif (item["f2"] == "low"):
            dataf2["low"].append(item["iClass"])

    return dataf2


def analyzef3(dataset):
    dataf3 = {"4": [], "3": [], "1": []}

    for item in dataset:
        if (item["f3"] == 4):
            dataf3["4"].append(item["iClass"])
        elif (item["f3"] == 3):
            dataf3["3"].append(item["iClass"])
        elif (item["f3"] == 1):
            dataf3["1"].append(item["iClass"])

    return dataf3


def analyzef4(dataset):
    dataf4 = {"6": [], "4": [], "1": []}

    for item in dataset:
        if (item["f4"] == 6):
            dataf4["6"].append(item["iClass"])
        elif (item["f4"] == 4):
            dataf4["4"].append(item["iClass"])
        elif (item["f4"] == 1):
            dataf4["1"].append(item["iClass"])

    return dataf4


def analyzef5(dataset):
    dataf5 = {"big": [], "medium": [], "small": []}

    for item in dataset:
        if (item["f5"] == "big"):
            dataf5["big"].append(item["iClass"])
        elif (item["f5"] == "medium"):
            dataf5["medium"].append(item["iClass"])
        elif (item["f5"] == "small"):
            dataf5["small"].append(item["iClass"])

    return dataf5


def analyzef6(dataset):
    dataf6 = {"high": [], "medium": [], "low": []}

    for item in dataset:
        if (item["f6"] == "high"):
            dataf6["high"].append(item["iClass"])
        elif (item["f6"] == "medium"):
            dataf6["medium"].append(item["iClass"])
        elif (item["f6"] == "low"):
            dataf6["low"].append(item["iClass"])

    return dataf6


def getCounts(analyzedDataset):
    countedArr = []

    for key, value in analyzedDataset.items():
        countedArr.append({"Q": value.count("Q"), "R": value.count("R"), "S": value.count("S"), "P": value.count("P"), "total": (value.count("Q") +
                                                                                                                                 value.count("R") + value.count("S") + value.count("P"))})
        print("Classification: {}".format(key))
        print("Q counts: {}".format(value.count("Q")))
        print("R counts: {}".format(value.count("R")))
        print("S counts: {}".format(value.count("S")))
        print("P counts: {}".format(value.count("P")))
        print("Total: {}".format(value.count("Q") +
                                 value.count("R") + value.count("S") + value.count("P")))

    return countedArr


test = [1/2, 1/2]


def calculateEntropy(countedArr):

    return entropy(test, None, 2)


def printData(dataSet):
    for key, value in dataSet.items():
        print("Classification: {}".format(key))
        print(value)


# print(" FEATURE 1:")
# printData(analyzef1(dataSet))
# print("\n FEATURE 2:")
# printData(analyzef2(dataSet))
# print("\n FEATURE 3:")
# printData(analyzef3(dataSet))
# print("\n FEATURE 4:")
# printData(analyzef4(dataSet))
# print("\n FEATURE 5:")
# printData(analyzef5(dataSet))
# print("\n FEATURE 6:")
# printData(analyzef6(dataSet))
print(getCounts(analyzef1(dataSet)))
print(calculateEntropy(test))
