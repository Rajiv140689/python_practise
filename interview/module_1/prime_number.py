import math
class Sample():
    def sample(self):
        n=24

        if n < 2:
            print("not a prime")
            return

        if n == 2:
            print("prime number")
            return

        if n%2==0:
            print("not a prime")
            return

        for i in range(3, int(math.sqrt(n))+1, 2):
            if n%i == 0:
                print("not a prime")
                return

        print("prime number")

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()