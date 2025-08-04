def main():
    tweet = input("Enter your tweet: ")
    print(twttr(tweet))

def twttr(word):
    for i in word:
        if i == "a" or i == "e" or i == "i" or  i == "o" or i == "u":
            word = word.replace(i,"")
        elif i == "A" or i == "E" or i == "I" or  i == "O" or i == "U":
            word = word.replace(i,"")
        else:
            word = word
    return word


main()