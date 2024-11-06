import math

class Sample():
    def sample(self):
        n=24
        count=0
        for i in range(1, int(math.sqrt(24))+1):
            # print(f"i: {i}")
            if n%i ==0:
                # print(f"factor i: {i}")
                # print("test", int(math.sqrt(n)))
                # print("test1", n//i)
                if i == (n//i):
                    # print("if block")
                    count+=1
                else:
                    # print("else block")
                    count+=2

        print(f"factors count: {count}")

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()