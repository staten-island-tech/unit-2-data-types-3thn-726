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

def login(password):
    #if statement evaluates to true we go to next line
    if password == "secret":
        print("logged in")
    else:
        print("incorrect")
x = input("what is the password?")
login(x)

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

""" food = (input("Give me a food:"))
print(type(food))
name = (input("Give me a name:"))
print(type(name))
adjective = (input("Give me a adjective:"))
print(type(adjective))
noun = (input("Give me a name:"))
print(type(noun))
food1 = (input("Give me another food:"))
print(type(food1))
name1 = (input("Give me another name:"))
print(type(name1)) """




