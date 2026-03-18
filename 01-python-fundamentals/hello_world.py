#My interactive developer profile
name = input ("What´s your name? ")
age = input ("How old are you? ")
specialization = input ("What do you what to specialize in? ")

print("-----------------")
print("Developer profile")
print("-----------------")
print("Name:", name)
print("Age:", age)
print("Specialization:", specialization)
print("-----------------")


#The program make decisions
age = int(age)
if age < 18:
    print("You are a junior developer training!")
elif age >= 18 and age <= 25:
    print("You are the perfect age to become an AI expert!")
else:
    print("Experience is you greatest advantage!")