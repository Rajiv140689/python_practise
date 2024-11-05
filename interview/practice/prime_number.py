from math import sqrt

class Sample():
    def sample(self):
        n1=12
        n=17
        if n <= 1:
            print("Not a Prime")
            return

        if n==2:
            print("Prime Number")
            return

        if n%2==0:
            print("Not a Prime")
            return

        '''
        Starting from 3 and using a step of 2 helps to:
        Eliminate unnecessary checks against even numbers (after confirming n is odd).
        '''
        for i in range(3, int(sqrt(n))+1, 2):
            if n%i==0:
                print("Not a Prime")
                return

        print("Prime Number")

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()