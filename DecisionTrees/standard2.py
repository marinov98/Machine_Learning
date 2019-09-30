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


def getOriginal(dataset):
    countQ = 0
    countP = 0
    countS = 0
    countR = 0
    for obj in dataset:
        if (obj["iClass"] == 'Q'):
            countQ += 1
        elif (obj["iClass"] == 'P'):
            countP += 1
        elif (obj["iClass"] == 'R'):
            countR += 1
        elif (obj["iClass"] == 'S'):
            countS += 1
    distribution = [countQ / len(dataset), countP /
                    len(dataset), countR/len(dataset), countS / len(dataset)]

    return entropy(distribution, None, 2)


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
    dataf3 = {"6": [], "4": [], "3": [], "1": []}

    for item in dataset:
        if (item["f3"] == 6):
            dataf3["6"].append(item["iClass"])
        elif (item["f3"] == 4):
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

    for value in analyzedDataset.values():
        countedArr.append({"Q": value.count("Q"), "R": value.count("R"), "S": value.count("S"), "P": value.count("P"), "total": (value.count("Q") +
                                                                                                                                 value.count("R") + value.count("S") + value.count("P"))})
    return countedArr


def entropies(countedDataset):
    distribution = []
    entropies = []
    for obj in countedDataset:
        for key, value in obj.items():
            if (key == "total"):
                if (len(distribution) > 0):
                    entropies.append(entropy(distribution, None, 2))
                    distribution.clear()
            elif (value > 0):
                distribution.append(value/obj["total"])

    return entropies


def getAverage(countsArr, entropies):
    total = 0
    i = 0
    for obj in countsArr:
        total += (obj["total"] / len(dataSet)) * entropies[i]
        i += 1

    return total


def getIntrinsicInfo(stats):
    info = 0
    for item in stats:
        info -= (item["total"] / 12) * log(item["total"] / 12, 2)

    return info


def showGains():
    original = getOriginal(dataSet)

    statsf1 = getCounts(analyzef1(dataSet))
    statsf2 = getCounts(analyzef2(dataSet))
    statsf3 = getCounts(analyzef3(dataSet))
    statsf4 = getCounts(analyzef4(dataSet))
    statsf5 = getCounts(analyzef5(dataSet))
    statsf6 = getCounts(analyzef6(dataSet))

    intrinsicf1 = getIntrinsicInfo(statsf1)
    intrinsicf2 = getIntrinsicInfo(statsf2)
    intrinsicf3 = getIntrinsicInfo(statsf3)
    intrinsicf4 = getIntrinsicInfo(statsf4)
    intrinsicf5 = getIntrinsicInfo(statsf5)
    intrinsicf6 = getIntrinsicInfo(statsf6)

    entropiesf1 = entropies(statsf1)
    entropiesf2 = entropies(statsf2)
    entropiesf3 = entropies(statsf3)
    entropiesf4 = entropies(statsf4)
    entropiesf5 = entropies(statsf5)
    entropiesf6 = entropies(statsf6)

    averagef1 = getAverage(statsf1, entropiesf1)
    averagef2 = getAverage(statsf2, entropiesf2)
    averagef3 = getAverage(statsf3, entropiesf3)
    averagef4 = getAverage(statsf4, entropiesf4)
    averagef5 = getAverage(statsf5, entropiesf5)
    averagef6 = getAverage(statsf6, entropiesf6)

    print("Gain(f1): {}".format(original - averagef1))
    print("Gain(f2): {}".format(original - averagef2))
    print("Gain(f3): {}".format(original - averagef3))
    print("Gain(f4): {}".format(original - averagef4))
    print("Gain(f5): {}".format(original - averagef5))
    print("Gain(f6): {}".format(original - averagef6))

    print("\n\n Using Gain Ratio as Criterion")
    print("GainRatio(f1): {}".format((original - averagef1) / intrinsicf1))
    print("GainRatio(f2): {}".format((original - averagef2) / intrinsicf2))
    print("GainRatio(f3): {}".format((original - averagef3) / intrinsicf3))
    print("GainRatio(f4): {}".format((original - averagef4) / intrinsicf4))
    print("GainRatio(f5): {}".format((original - averagef5) / intrinsicf5))
    print("GainRatio(f6): {}".format((original - averagef6) / intrinsicf6))


def printData(dataSet):
    # the getCounts will return an array of dictionaries with the count of how often each class occurs as well as the total
    statsf1 = getCounts(analyzef1(dataSet))
    statsf2 = getCounts(analyzef2(dataSet))
    statsf3 = getCounts(analyzef3(dataSet))
    statsf4 = getCounts(analyzef4(dataSet))
    statsf5 = getCounts(analyzef5(dataSet))
    statsf6 = getCounts(analyzef6(dataSet))

    entropiesf1 = entropies(statsf1)
    entropiesf2 = entropies(statsf2)
    entropiesf3 = entropies(statsf3)
    entropiesf4 = entropies(statsf4)
    entropiesf5 = entropies(statsf5)
    entropiesf6 = entropies(statsf6)

    print("\nOriginal Entropy")
    print(getOriginal(dataSet))
    print("\n")

    # for each feature the entropies function will return an array of all the entropies for that feature
    print("Feature 1 stats:\n")
    print(statsf1)
    print("Entropies when splitting on feature 1:\n")
    print(entropiesf1)
    print("\nEntropy average for feature 1:")
    print(getAverage(statsf1, entropiesf1))
    print("\n\n")
    print("Feature 2 stats:\n")
    print(statsf2)
    print("Entropies when splitting on feature 2:\n")
    print(entropiesf2)
    print("\nEntropy average for feature 2:")
    print(getAverage(statsf2, entropiesf2))
    print("\n\n")
    print("Feature 3 stats:\n")
    print(statsf3)
    print("Entropies when splitting on feature 3:\n")
    print(entropiesf3)
    print("\nEntropy average for feature 3:")
    print(getAverage(statsf3, entropiesf3))
    print("\n\n")
    print("Feature 4 stats:\n")
    print(statsf4)
    print("Entropies when splitting on feature 4:\n")
    print(entropiesf4)
    print("\nEntropy average for feature 4:")
    print(getAverage(statsf4, entropiesf4))
    print("\n\n")
    print("Feature 5 stats:\n")
    print(statsf5)
    print("Entropies when splitting on feature 5:\n")
    print(entropiesf5)
    print("\nEntropy average for feature 5:")
    print(getAverage(statsf5, entropiesf5))
    print("\n\n")
    print("Feature 6 stats:\n")
    print(statsf6)
    print("Entropies when splitting on feature 6:\n")
    print(entropiesf6)
    print("\nEntropy average for feature 6:")
    print(getAverage(statsf6, entropiesf6))

    print("\n\n Using Entropy Criterion")
    showGains()

###############
# Output
###############


printData(dataSet)
