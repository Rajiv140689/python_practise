class Sample():
    def expand_around_center(self, s, left, right):
        palindrome_substring=""
        max_len=0
        while left>0 and right<len(s) and s[left] == s[right]:
            if (right-left+1)>max_len:
                max_len=right-left+1
                palindrome_substring = s[left:right+1]
            left-=1
            right+=1

        return palindrome_substring

    def sample(self):
        s="babad"
        n= len(s)
        result=""
        for i in range(n):
            odd = self.expand_around_center(s, i, i)
            even = self.expand_around_center(s, i, i+1)

            if len(odd) > len(result):
                result=odd

            if len(even) > len(result):
                result=even

        print(f"result: {result}")

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()