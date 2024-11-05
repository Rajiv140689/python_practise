class Sample():
    def sample(self):
        val = 1234
        rev=0
        while val > 0:
            mod_val = val%10
            val = val//10
            rev = rev*10+mod_val

        print(rev)

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()


