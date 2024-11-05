class Sample():
    def sample(self):
        sorted_dup_arr=['a','a','a','b','c','d','d','e','g']

        if not sorted_dup_arr:
            print("empty string")
        j=1
        for i in range(1, len(sorted_dup_arr)):
            if sorted_dup_arr[i]!=sorted_dup_arr[i-1]:
                sorted_dup_arr[j]=sorted_dup_arr[i]
                j+=1

        #for remaing data setting the value as ''
        while j<len(sorted_dup_arr):
            sorted_dup_arr[j]=''
            j+=1

        print(sorted_dup_arr)

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()


