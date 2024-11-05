class Sample():
    def sample(self):
        num_of_stairs=6
        total_moves=3
        total_path_count=[0]*(num_of_stairs+1)
        total_path_count[0]=1

        for i in range(1, num_of_stairs+1):
            for j in range(1,total_moves+1):
                if i-j>=0:
                    total_path_count[i]+=total_path_count[i-j]

        print(total_path_count[num_of_stairs])

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()