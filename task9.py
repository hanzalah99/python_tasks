
""""
def distinct_words(words):
    for index in range(0,len(words)):
        for index2 in range(1,len(words)):

"""
def occurances(words):
    occurances_words = 1
    temp=len(words)
    for index in range(0,temp):
        for index2 in range(0,temp):
            if(words[index]==words[index2] and index!=index2):
                occurances_words+=1
                words.pop(index2)
                temp-=1
        print(occurances_words)
        occurances_words=1


def main():
    total_words=int(input('Enter the no of words: '))
    words = []

    for index in range(0,total_words):
        item=input()
        words.append(item)
    
    occurances(words)
    print(words)
if __name__ == "__main__":
    main()
