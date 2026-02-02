#Magic8Ball.py
#Name: Emma Zechmann
#Date: 2/1/2026
#Assignment: MAgic Eight ball 

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
    print("Magic 8 Ball")
  #Prompt the user for their question.
    question = input("what is your question: ")
    print(input)
    Response = ["ew, no!" , "Absolutely" , "I guess so?", "Most likely", "Ask Again Later" , "Don't Count on It", "It is certain"]
    Answer = random.choice(Response)
    print(Answer)
  #Answer question randomly with one of the options from your earlier list.


if __name__ == '__main__':
  main()
