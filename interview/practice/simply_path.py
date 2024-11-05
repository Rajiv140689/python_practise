import re

class Sample():
    def sample(self):
        inp = "/a/b/c/../././//d"
        inp_list=re.split('/+', inp)
        new_path_list = []
        print(inp_list)
        for char in inp_list:
            if char != '..' and char != '.' and char != ' ':
                new_path_list.append(char)
            elif char == '..' and new_path_list:
                new_path_list.pop()

        print(new_path_list)

        print("/"+"/".join(new_path_list))

if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()