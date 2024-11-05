class Sample():
    def sample(self):
        s = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'a', 'a']
        i=0
        j=0
        while i < len(s):
            curr_char = s[i]
            count=0
            while i < len(s) and s[i] == curr_char:
                count+=1
                i+=1

            s[j] == curr_char
            j+=1

            if count>1:
                for digit in str(count):
                    s[j]=digit
                    j+=1

        print(f"compressed string: {s[:j]}")

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()