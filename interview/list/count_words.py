
class CountWord:
    def count_words(self):
        str = "I am name is Avayan Pratap Singh"
        word_list = str.split(" ")
        count = len(word_list)

        print("word count: ", count)

if __name__ == "__main__":
    countWordObj = CountWord()
    countWordObj.count_words()