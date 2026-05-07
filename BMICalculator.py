# This is a BMI Calculator
weight = float(input("Entre your weight in kg "))
height = float(input("Enter your height in m "))
print(f"Your weight is {weight}kg. Your height is {height}m.")
BMI = weight / (height ** 2)
print(f"Your BMI is {round(BMI, 1)}.")

# BMI classification and health advice
if BMI < 18.5:
    print ("Classification: Underweight")
    pring ("Advice: Increase your calorie intake with nutritious foods, incorporate strength training to build muscle mass, and consider consulting a dietitian.")
elif BMI < 25:
    print("Classification: Normal")
    print("Advice: Keep up your healthy lifestyle! Maintain a balanced diet and regular exercise routine, and schedule periodic health check-ups.")
elif BMI < 30:
    print("Classification: Overweight")
    print("Advice: Reduce high-calorie food intake, increase aerobic exercise such as jogging or swimming, and aim for at least 150 minutes of exercise per week.")
else:
    print("Classification: Obese")
    print("Advice: Consult a doctor or dietitian as soon as possible to develop a safe weight-loss plan, and monitor key health indicators such as blood pressure and blood sugar regularly.")