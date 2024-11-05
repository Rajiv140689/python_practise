class Sample():
    def sample(self):
        inp=["flower", "flow", "flight"]
        # inp=["dog","racecar","car"]
        # inp=["",""]
        # inp = ["","a"]

        if not inp or all(s == "" for s in inp):
            return ""

        for i in range(len(inp[0])):
            for word in inp:
                if i>=len(word) or inp[0][i] != word[i]:
                    print(inp[0][:i])
                    return

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()