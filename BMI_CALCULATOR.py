#BODY MASS INDEX

Name=input("enter name:")
Age=int(input("enter age:"))
Gender=input("enter gender:")
print(Name)
print(Age)
print(Gender)

weight=float(input("enter weight in kg:"))
height=float(input("enter height in meter:"))
BMI=weight/(height*height)
print("BMI:",BMI)

if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("overweight")
else:
    print("obese")
