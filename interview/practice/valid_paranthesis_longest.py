class Sample():
    def sample(self):
        input = "))(())"
        paranthesis_list=[-1]
        max_len=0

        '''
            initially we assign -1
            we pop the element and calculate the size -> 
            example "))(())" -> 0,1,2,3,4,5
            => step 1 -> -1 is popped and we stored 0
               step 2 -> 0 is popped and we stored 1
               step 3 -> 2 is stored
               step 4 -> 3 is stored
               step 5 -> 3 is popped and max_len = current_index - value before popped = 4-2 = 2
               step 5 -> 2 is popped and max_len = current_index - value before popped = 5-1 = 4
            if -1 is popped then we push current element index
        '''
        for i in range(len(input)):
            if input[i] == '(':
                paranthesis_list.append(i)
            else:
                paranthesis_list.pop()
                if not paranthesis_list:
                    paranthesis_list.append(i)
                else:
                    max_len=max(max_len, i-paranthesis_list[-1])

        print(max_len)


if __name__ == "__main__":
    sampleObj = Sample()
    sampleObj.sample()