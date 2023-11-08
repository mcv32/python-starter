import random

def main():
    #ex2()
    # ex3()
    # ex4()
    #ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    # ex11()
    # ex12()
    #  ex13()
     ex14()

def ex2():
    width = (float) (input("Enter a width: "))
    height = (float) (input("Enter a height: "))
    length = (float) (input("Enter a length: "))
    print("Volume is: " + str(round(width * height * length, 2)))

def ex3():
    numList = []
    
    while(True):
        number = input("Enter number: ")
            
        if number == "quit":
            break
        
        num = int(number)
        numList.append(num)

    if numList[0] != numList[len(numList)-1]:
        print(False)
    else:
        print(True)

def ex4():
    paragraph = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    words = paragraph.split(" ")
    count = 0
    for x in range(len(words)):
        if "Python" in words[x]:
            count += 1
    print(count)

def ex5():
    myList = [1,2,3]
    mySet = {3,4,5}

    for i in range(len(myList)):
        mySet.add(myList[i])

    print(mySet)

def ex6():
    myList = [11, 100, 101, 999, 1001]
    myList.reverse()
    print(myList)

def ex7():
    randon = random.randint(1,100)
    if randon < 10:
        print(str(randon) + ": You lose")
    elif randon < 50:
        print(str(randon) + ": Try again")
    else:
        print(str(randon) + ": You win!")

def ex8():
    myList = [6,2,7,3,77,7,1]
    lowest = myList[0]
    for i in range(len(myList)):
        if lowest > myList[i]:
            lowest = myList[i]

    print(lowest)

def ex9():
    word = "HELLO"
    print(word.isupper())

def ex10():
    vowels = 0
    consonants = 0
    word = input("Enter a word: ")
    lowercase = word.lower()
    for i in range(len(word)):
        if(lowercase[i] == "a" or lowercase[i] == "e" or 
           lowercase[i] == "i" or lowercase[i] == "o" or lowercase[i] == "u"):
            vowels += 1
        else:
            consonants += 1
    print("Vowels: " + str(vowels))
    print("Consonants: " + str(consonants))

def ex11():
    date = "11/8/2023"
    output = "Today's date is: {}".format(date)
    f = open("output.txt", "w")
    f.write(output)
    f.close()

def ex12():
    num = str(input("Enter a number: " ))
    if (num[0] == "-"):
        print(num[1:])
    elif (num.find(".") != -1):
        print("error: " + num + " is not an integer")
    else:
        print("-" + num)

def ex13():
    while (True):
        num1 = input("Enter first integer: ")
        if (num1 == "exit"):
            break
        num2 = input("Enter second integer: ")
        if (num2 == "exit"):
            break
        sum = int(num1) + int(num2)
        print("Answer: " + str(sum))

def ex14():
    while (True):
        num1 = input("Enter first integer: ")
        if (num1 == "exit"):
            break
        num2 = input("Enter second integer: ")
        if (num2 == "exit"):
            break
        operation = input("Enter operation (add, sub, mul, div): ")

        if (operation.lower() == "add"):
            result = int(num1) + int(num2)
            print("Answer: " + str(result))
        elif (operation.lower() == "sub"):
            result = int(num1) - int(num2)
            print("Answer: " + str(result))
        elif (operation.lower() == "mul"):
            result = int(num1) * int(num2)
            print("Answer: " + str(result))
        else:
            result = int(num1) / int(num2)
            print("Answer: " + str(result))

if __name__ == "__main__":
    main()