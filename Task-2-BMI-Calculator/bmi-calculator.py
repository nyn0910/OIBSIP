def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value

        except ValueError:
            print("Invalid input! Please enter a number.")


print("===== BMI CALCULATOR =====")

weight = get_positive_number("Enter your weight in kg: ")
height = get_positive_number("Enter your height in metres: ")

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("\n===== YOUR RESULT =====")
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")
