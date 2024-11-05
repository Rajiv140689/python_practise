class Sample():
    def sample(self):
        #get prefix and suffix and multiply prefix and suffix to get result
        val_list=[2,1,3,5,6]
        prefix_curr, suffix_curr=1, 1
        n=len(val_list)
        prefix_list=[1]*n
        result=[1]*n
        #get prefix
        for i in range(n):
            prefix_list[i]=prefix_curr
            prefix_curr=prefix_curr * val_list[i]

        print(f"prefix_list: {prefix_list}")

        #get suffix and multiply with prefix_list to get
        # example for 3 = prefix = 2*1 and suffix = 5*6 and result is prefix * suffix
        for i in range(n-1, -1, -1):
            result[i]=suffix_curr * prefix_list[i]
            suffix_curr=suffix_curr*val_list[i]

        print(result)

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()
