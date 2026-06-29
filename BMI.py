weight = float(input("Enter your weightin kg: "))
height_feet = float(input("Enter your height in feet: "))
height_inches = float(input("Enter your height in inches: "))

total_feet = height_feet + (height_inches /12)
height_meters = total_feet * 0.3048
squared_height = height_meters * height_meters
BMI = weight / squared_height

if BMI < 18.5:
    print("BMI = ", BMI, "Underweight.")

elif BMI >= 18.5 and BMI < 25.0:
    print("BMI = ", BMI, "Healthy weight.")

elif BMI >= 25.0 and BMI < 30.0:
    print("BMI = ", BMI, "Overweight.")

elif BMI >= 30.0:
    print("BMI = ", BMI)