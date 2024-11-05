class GasAndCost():
    def gasAndCost(self):
        gas = [5,1,2,3,4]
        cost = [4,4,1,5,1]

        totalGasInTank=0
        additionalGasNeeded=0
        for i in range(len(gas)):
            totalGasInTank = totalGasInTank + (gas[i]-cost[i])
            if totalGasInTank < 0:
                additionalGasNeeded = additionalGasNeeded + totalGasInTank
                totalGasInTank = 0
                startStation=i+1

        if additionalGasNeeded+totalGasInTank>=0:
            print(f"startStation: {startStation}")
        else:
            print(f"startStation: -1")

if __name__ == "__main__":
    sampleObj = GasAndCost()
    sampleObj.gasAndCost()