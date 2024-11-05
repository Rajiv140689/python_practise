class Sample():
    def sample(self):
        str = "Hey Avyan"

        #1st way
        reverse_str =""
        for char in str:
            reverse_str = char + reverse_str

        print(reverse_str)

        # second way
        str = str[::-1]
        print(str)

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()


