class Sample():
    def sample(self):
        val1="{{}}[]((())"
        val2="{[{()}]}{{}}"
        paran_list=[]
        paran_dict = {')': '(', '}': '{', ']': '['}

        for char in val2:
            if char in paran_dict.values():
                paran_list.append(char)
            elif char in paran_dict.keys():
                if not paran_list and paran_list[-1]!=paran_dict[char]:
                    return False

                paran_list.pop()

        if not paran_list:
            print("Valid Paranthesis")
        else:
            print("Not Valid Paranthesis")


if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()


