# TODO: Create a string variable with a sentence
phrase = " Hi! my name is Kevin "

# TODO: Convert the string to uppercase
phrase_up = phrase.upper()

# TODO: Convert the string to lowercase
phrase_low = phrase.lower()

# TODO: Capitalize the first letter of each word
phrase_title = phrase.title()

# TODO: Replace a word in the string
phrase_replace = phrase.replace("Kevin", "John")

# TODO: Split the string into a list of words
phrase_split = phrase.split("!")

# TODO: Join the list of words back into a string using a different separator
phrase_joined = ",".join(phrase_split)

# TODO: Find the position of a specific word in the string
phrase_find = phrase.find("Kevin")

# TODO: Check if the string starts with a specific word
start_Hi = phrase.startswith(" Hi!")

# TODO: Remove leading and trailing whitespace from a string
phrase_strip = phrase.strip()

# Print the results of each operation

# print(phrase)
# print(phrase_up)
# print(phrase_low)
# print(phrase_title)
# print(phrase_replace)
# print(phrase_split)
# print(phrase_joined)
# print(phrase_find)
# print(start_Hi)
# print(phrase_strip)

# TODO: Create variables for name, age, and height
name = "Kevin"
age = 25
height = 1.91

# TODO: Use the .format() method to create a sentence with these variables
sentence_f = "my name is {}, I'm {} years old and I'm {} meters tall."
# print(sentence_f.format(name, age, height))

# TODO: Use f-strings to create the same sentence
sentence_fstr = f"my name is {name}, I'm {25} years old and I'm {1.91} meters tall."

# TODO: Use the % operator for string formatting
# sentence_pourcent = "my name is %s, I'm %d years old and I'm %.2f meters tall."
# print(sentence_pourcent.%(name, age, height))

# TODO: Format a float number to display only two decimal places
pi = 3.1415926535
pi_formatted = f"{pi:.2f}"
# print(f"{pi:.2f}")

# TODO: Create a table-like output using string formatting
# Print all formatted strings


# TODO: Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# TODO: Use a for loop to print each number in the list
# for x in numbers:

# TODO: Use a for loop with enumerate() to print both index and value
# for index, value in enumerate(numbers):
   # print(index, ":", value)


# TODO: Create a dictionary and use a for loop to print all keys and values
person = {"name": "Kevin", "age": 25, "city": "Compiègne"}

# for keys, values in person.items():
   # print(f"{keys} : {values}")

# TODO: Use a for loop with range() to print numbers from 1 to 10

# for i in range(1, 11): print(i)

# TODO: Use list comprehension to create a new list of squares of numbers
squares = [x**2 for x in numbers]
# print(squares)

# TODO: Use a nested for loop to create a multiplication table (up to 5x5)

# Exercice 4
# TODO: Use a while loop to print numbers from 1 to 10
# i = 1
# while i < 11:
   # print(i, end=" ")
   # i += 1

# TODO: Create a guessing game using a while loop
# (generate a random number and let the user guess until correct)
number = 5
x = 0
while x != number:
   x = int(input("enter a number between 1 and 10 :"))
   if x > number:
      print("too high")
   elif x < number:
      print("too low")
   else:
      print("You won !")

# TODO: Use a while loop to calculate the factorial of a number
n = int(input("Enter a number"))
i = 0
fact = 1

while i <= n:
   i += 1
   fact *= i
print(f"the factorial of {n} is {fact}")

# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)
