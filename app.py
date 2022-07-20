import json
from difflib import get_close_matches


data = json.load(open("076 data.json"))

def translate(word):
    if word in data:

        return data[word]
    else:
        closeword = get_close_matches(word, data, n=1, cutoff=0.8)
        if closeword == []:
            return "Enter a correct word."
        else:
            print("Did you mean ", closeword)
            final = ""
            y_n = input("Enter Y/N : ")
            if y_n == "y":
                for i in closeword[0]:
                    final = final + i
                return data[final]
            else:
                return "Enter a valid word"


def main():

    word = input("Enter the word : ")
    word  = word.lower()
    print(translate(word))


main()
