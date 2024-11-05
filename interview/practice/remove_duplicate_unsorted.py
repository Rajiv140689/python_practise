class Sample():
    def sample(self):
        dup_unsorted_arr=['a', 'b', 'a', 'a', 'c', 'd', 'e', 'd', 'f']

        if not dup_unsorted_arr:
            print("empty array/list")

        unique_set = set()

        j=1
        unique_set.add(dup_unsorted_arr[0])
        for i in range(1, len(dup_unsorted_arr)):
            if dup_unsorted_arr[i] not in unique_set:
                unique_set.add(dup_unsorted_arr[i])
                dup_unsorted_arr[j]=dup_unsorted_arr[i]
                j+=1

        while j < len(dup_unsorted_arr):
            dup_unsorted_arr[j]=''
            j+=1

        print(dup_unsorted_arr)

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()


