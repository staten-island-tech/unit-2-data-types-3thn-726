#Strings are for representing characters, names, words, etc.
#name= "deivid"
#integers represent whole numbers
#age: 14
#Floats represents decimals
#wallet: 5.45
#booleans represents true/false, used in evaluations
#graduated = False
#input asks the user a question and stores their response as a value
#Lists
#students = ("Joanna", "Deivid", "David", "Other David", "Ethan")
#similar to saying for i in range(5): print(students[i])
""" print(students[4])
for student in students:
    print(student) """

""" moneys = [1,2,3,4,5,6]
total: 0
for money in moneys:
 """

""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

#calculator
""" bill = float(input("Bill cost:"))
print(type(bill))
tip = float(input("Tip amount:"))
print(type(tip))
total = (float(bill + tip))
print("The total is", total) """

#character calculator
""" string = (input("Words/Characters:"))
print(type(string))
length=len(string)
print("The length of those words/characters is:", length) """

""" def login(password):
    #if statement evaluates to true we go to next line
    if password == "secret":
        print("logged in")
    else:
        print("incorrect")
x = input("what is the password?")
login(x) """

""" def grade(score):
    if score >= 92:
        print("A")
    elif score >= 82:
        print("B")
    elif score >= 72:
        print("C")
    else:
        print("F")
x = int(input("What's the score?"))
grade(x) """

""" def gamble(age, id):
    if age >= 21 and id == True:
        print("Gamble away")
    elif age >= 21 and id == False:
        print("You need ID verification")
    else:
        print("You're too young") """

""" raining = False
if not raining == true:
    print("go for a walk")
if raining == false:
    print("go for a walk") """

""" food = (input("Give me a food:"))
print(type(food))
name = (input("Give me a male celebrities name:"))
print(type(name))
verb = (input("Give me a past tense verb:"))
print(type(verb))
adjective = (input("Give me a adjective:"))
print(type(adjective))
noun = (input("Give me a noun:"))
print(type(noun))
number = (input("Give me a number:"))
print(type(number))
verb2 = (input("Give me another verb:"))
print(type(verb2))
print("Me and my friend decided to get", food, ". Then, my friend", name, "forgot he had a class he had to go to. So he", verb, "his way to his class, but bumped into a", adjective, "looking man. After he got a lecture from the guy, he jumped onto a", noun, ", which almost got him arrested so he", verb2, "away. He then got jumped by", number,"men in children's underwear, So he boarded a flight to North Korea and was never seen again.")

 """

#Check i X is a factor Modulo
#if factor == true add to list
#loop from 2 to Y for i in range(2,15)
#if x isFactor and y isFactor then add to list

""" number = int(input("Number:"))
print(type(number))

if number % 2 == 0:
    print("Your number is Even!")
else:
    print("Your number is odd!") """

""" bill = float(input("Bill Cost:"))
print(type(bill))
print("How was Service? Please choose an option:")
print("1. Service was bad")
print("2. Service was okay")
print("3. Service was good")
print("4. Service was great")
choice = input("Enter the number of your choice: ")
if choice == '1':
    print("Your total is", bill + bill*0)
elif choice == '2':
    print("Your total is", bill + bill*0.15)
elif choice == '3':
    print("Your total is", bill + bill*0.2)
elif choice == '4':
    print("Your total is", bill + bill*0.25)
else:
    print("Invalid choice, please choose a number between 1 and 4.") """

""" def factorfinder():
    number = int(input("Number:"))
    print(type(number))
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
                factors.append(i)
    return factors

factors = factorfinder()
print(f"The factors are: {factors}") """

""" def gcf():
    number1 = int(input("1st Number:"))
    number2 = int(input("2nd Number:"))

    print(type(number1))
    print(type(number2))

    factor1 = []
    factor2 = []
    same_numbers = []

    for number in range(1, number1 + 1):
        if number1 % number == 0:
            factor1.append(number)

    for number in range(1, number2 + 1):
        if number2 % number == 0:
            factor2.append(number)

    for number in factor1:
        if number in factor2:
            same_numbers.append(number)
    
    gcf = max(same_numbers)
    print("The GCF of your numbers is:", gcf)
gcf() """

""" def skins(money, age, isAvailable):
    cost = int(input("cost:"))
    money = int(input("Money:"))
    age = int(input("Age:"))
    if isAvailable == False:
        return ("cannot buy")
    if isAvailable == True:
        if age < 18:
            return ("cannot buy")
        else:
            if money >= cost:
                return ("can buy")
            else:
                return ("cannot buy") """
            




import random
numbers = [1,2,3,4,5,6,7,8,9,10]
random_number = random.choice(numbers)
number_guessed = int(input("Number:"))
numbers_that_have_been_guessed = []
while number_guessed != random_number:
    if number_guessed < random_number:
        numbers_that_have_been_guessed.append(number_guessed)
        number_guessed = int(input("Higher, try again:"))
    else:
        numbers_that_have_been_guessed.append(number_guessed)
        number_guessed = int(input("Lower, try again:"))
if number_guessed == random_number:
    numbers_that_have_been_guessed.append(number_guessed)
    print("Correct! The number was ", number_guessed)
    print("Your guess history is:", numbers_that_have_been_guessed)

""" def english_or_french():
    t_T = 0
    s_S = 0
    text = input("Text:")

    for letters in text:
        if letters in text == "t" or "T":
            t_T + 1
        if letters in text == "s" or "S":
            s_S + 1

    if t_T >= s_S:
        print("Your text might be english")
    else:
        print("Your text might be french")
english_or_french() """

