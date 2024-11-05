class CandyCount():
    def candyCount(self):
        ratings=[1,0,2,1,3,1]
        #By default everyone should get one candy
        candy=[1]*len(ratings)

        #Left side -
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1

        #Right side -
        for i in range(len(ratings)-2, -1,-1):
            if ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i], candy[i+1]+1)

        totalCandy =0
        for candy_val in candy:
            totalCandy +=candy_val

        print(f"totalCandy: {totalCandy}")


if __name__ == "__main__":
    candyCountObj= CandyCount()
    candyCountObj.candyCount()


