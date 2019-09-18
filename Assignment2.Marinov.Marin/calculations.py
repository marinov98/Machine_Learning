##########################
# Datasets
##########################

dataset = {
    2: 0.3,
    4: 0.2,
    8: 0.2,
    16: 0.06,
    32: 0.21,
    64: 0.03
}

equalDiceChance = 1.0 / 6


fairDataset = {
    2: equalDiceChance,
    4: equalDiceChance,
    8: equalDiceChance,
    16: equalDiceChance,
    32: equalDiceChance,
    64: equalDiceChance
}

######################
# Functions
#####################


def calculateExpectedValue(dataSet):
    mean = 0

    for key, value in dataSet.items():
        mean += key * value

    return mean


def calculateVariance(dataSet):
    variance = 0
    mean = calculateExpectedValue(dataSet)

    for key, value in dataSet.items():
        variance += ((key - mean) ** 2) * value

    sd = variance ** 0.5

    return (variance, sd)


def calculateTenTosses(dataSet):
    expected = 10 * calculateExpectedValue(dataSet)
    variance, sdz = calculateVariance(dataSet)
    sdz = (variance * 10) ** 0.5

    return (expected, variance*10, sdz)


def printResults(dataSet):
    mean = calculateExpectedValue(dataSet)

    variance, sd = calculateVariance(dataSet)

    meanz, variancez, sdz = calculateTenTosses(dataSet)

    print("\nMean of discrete random variable: {}".format(mean))
    print("Standard Deviation of discrete random variable: {} \nVariance of discrete random variable: {}".format(sd, variance))
    print("\n10 Independent events Mean: {}".format(meanz))
    print("10 Independent events Variance: {}".format(variancez))
    print("10 Independent events Sd: {}".format(sdz))

##################################
# Mean, SD, and Variance results:
##################################


printResults(dataset)
printResults(fairDataset)
