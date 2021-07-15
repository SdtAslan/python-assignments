# first method

age_75_over_and_smoking = True
chronic = True
Weak_immune = True
if age_75_over_and_smoking and chronic and Weak_immune == True:
    print("You are in risky group")
else:    
    print("You are not in risky group")
    
# second method

age = int(input("Enter your age: "))
if int(age) >= 75:
    age = True
elif int(age) <= 74:
    age = False
x = str(input("are you addicted to smoking (Yes or No):")).strip().lower()
if x == "yes":
    x = True
elif x == "no":
    x = False
chronic = str(input("Do you have a severe chronic disease? (Yes or No): ")).strip().lower()
if chronic == "yes":
    chronic = True
elif chronic == "no":
    chronic = False
immune = str(input("Is your immune system too weak? (Yes or No): ")).strip().lower()
if immune == "yes": 
    immune = True
elif immune == "no":
    immune = False
risk_as_a_percent = bool(x and age) * 34  + bool(chronic) * 33 + bool(immune) * 33
if risk_as_a_percent >= 50:
    print("Your risk of death from coronavirus: %", risk_as_a_percent, "BE CAREFUL!")
else:    
    print("Your risk of death from coronavirus: %", risk_as_a_percent, "Don't be too confident though")

# https://github.com/SdtAslan/python-assignments.git
