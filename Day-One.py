print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.") 

#When executing Input code will be replaced with the input
print(len(input("What is your name?")))

#Learned about variable place holders as C is used below
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = str(a)
a = str(b)
b = str(c)

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#Final \n makes the input go to the next line for a cleaner look
#1. Create a greeting for your program.
print("Welcome to the best band name generator!")
#2. Ask the user for the city that they grew up in.
city = input("What city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What was the name of your first pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your awesome band name is " + city + " " + pet)
#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end
