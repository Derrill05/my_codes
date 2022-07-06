name=input("Enter your name: ")
height_m=float(input("Enter your height: "))
weight_kg=float(input("Enter your weight: "))

bmi=weight_kg/height_m**2

if bmi <18.5:
    print("Your BMI is :")
    print(bmi)
    print("Oops ! " + name + " is underweignt.")
elif bmi >= 18.5 and bmi <25:
    print("Your BMI is :")
    print(bmi)
    print ("GREAT!! " + name + " is in normal weight.")
elif bmi >= 25 and bmi < 30:
    print("Your BMI is")
    print(bmi)
    print("oops ! " + name + " is overweight.")
else:
    print("OOH NOO ! " + name + " is obese.")