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


def printResults(dataSet):
    mean = calculateExpectedValue(dataSet)

    variance, sd = calculateVariance(dataSet)

    print("\nMean of discrete random variable: {}".format(mean))
    print("Standard Deviation of discrete random variable: {} \nVariance of discrete random variable: {}".format(sd, variance))

##################################
# Mean, SD, and Variance results:
##################################


printResults(dataset)
printResults(fairDataset)