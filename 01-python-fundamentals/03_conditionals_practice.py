# Practice: variables, input, and conditionals

name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 18:
    print("Hello,", name, "- you are a minor.")
elif age <= 30:
    print("Hello,", name, "- you are a young adult.")
else:
    print("Hello,", name, "- you are an adult.")
    