class Sample():
    def sample(self):
        str="civic"
        left, right = 0, len(str)-1
        is_palindrome=True
        while left<right:
            if str[left]!=str[right]:
                print("Not a palindrome")
                is_palindrome=False
            left+=1
            right-=1

        if is_palindrome:
            print("Palindrome")

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()