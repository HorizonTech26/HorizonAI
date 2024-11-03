import random, datetime, os
from HorizonAI_Data import *

class Storage:
    def __init__(self, input, responces):
        self. input = input
        self.responces = responces

def Greeting():
    Greetings = ["Hi", "Hello", "What's up", "Whats up", "Howdy", "Sup", "Hey", "hi", "hello", "what's up", "whats up", "howdy", "sup", "hey"]
    for x in range(len(Greetings)):
        if Greetings[x] in HorizonAI.input:
            RandNum = random.randint(1, 3)
            if RandNum == 1:
                HorizonAI.responces.append("Hi!")
            elif RandNum == 2:
                HorizonAI.responces.append("Hello!")
            elif RandNum == 3:
                HorizonAI.responces.append("Yo!")

def AltGreeting():
    AltGreetings = ["How are you", "Howve you been", "How've you been", "how are you", "howve you been", "how've you been"]
    for x in range(len(AltGreetings)):
        if AltGreetings[x] in HorizonAI.input:
            RandNum = random.randint(1, 2)
            if RandNum == 1:
                HorizonAI.responces.append("I'm good, thanks for asking!")
            elif RandNum == 2:
                HorizonAI.responces.append("I'm good.")

def Time():
    today = datetime.datetime.now()
    if "Time" in HorizonAI.input or "time" in HorizonAI.input:
        HorizonAI.responces.append("The current time is " + today.strftime("%I:%M"))
    if "Date" in HorizonAI.input or "date" in HorizonAI.input:
        HorizonAI.responces.append("Today's date is " + today.strftime("%m/%d/%Y"))
    if "Day is it" in HorizonAI.input or "day is it" in HorizonAI.input:
        HorizonAI.responces.append("Today is " + today.strftime("%A"))
    if "Month" in HorizonAI.input or "month" in HorizonAI.input:
        HorizonAI.responces.append("The month is " + today.strftime("%B"))
    if "Year" in HorizonAI.input or "year" in HorizonAI.input:
        HorizonAI.responces.append("The year is " + today.strftime("%Y"))

def Joke_Fact():
    if "Joke" in HorizonAI.input or "joke" in HorizonAI.input:
        Num = str(random.randint(1, 15))
        HorizonAI.responces.append(Jokes[Num])
    if "Fact" in HorizonAI.input or "fact" in HorizonAI.input:
        Num = str(random.randint(1, 10))
        HorizonAI.responces.append(Facts[Num])

def Math():
    Num1 = ""
    Num2 = ""
    operator = ""
    operations = ["+", "-", "*", "/"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    if any(item in HorizonAI.input for item in operations) and any(item in HorizonAI.input for item in numbers):
        for char in range(len(HorizonAI.input)):
            if HorizonAI.input[char] in numbers:
                if operator == "":
                    Num1 += HorizonAI.input[char]
                else:
                    Num2 += HorizonAI.input[char]
            elif HorizonAI.input[char] in operations:
                operator = HorizonAI.input[char]
        Num1 = int(Num1)
        Num2 = int(Num2)
        if operator == "+":
            Answer = Num1 + Num2
        elif operator == "-":
            Answer = Num1 - Num2
        elif operator == "/":
            Answer = Num1 / Num2
        elif operator == "*":
            Answer = Num1 * Num2
        else:
            print("Math Error")
            return
        HorizonAI.responces.append("The answer to your equation is", Answer)

def ReadMemory():
    for key in Knowledge.keys():
        if key in HorizonAI.input:
            HorizonAI.responces.append(Knowledge[key])

def fin():
    finished = ["bye", "Bye", "done", "Done"]
    if any(item in HorizonAI.input for item in finished):
        return "exit"

def Respond():
    Responce = ""
    for item in range(len(HorizonAI.responces)):
        check = HorizonAI.responces[item]
        if check[-1] == "." or check[-1] == "?" or check[-1] == "!":
            Responce = Responce + HorizonAI.responces[item] + " "
        else:
            Responce = Responce + HorizonAI.responces[item] + ". "

    if Responce == "":
        print("Sorry, I can't help with that at the moment.")
    else:
        print(Responce)

print("Hi, I'm HorizonAI. Ask me anything!")
while True:
    Query = input()
    HorizonAI = Storage(Query, [])

    Greeting()
    AltGreeting()
    Time()
    Joke_Fact()
    Math()
    ReadMemory()
    done = fin()
    if done == "exit":
        break
    Respond()