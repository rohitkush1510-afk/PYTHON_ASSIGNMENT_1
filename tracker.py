'''
Name :Rohit Kushwaha                                                   
Date : 11/11/25
Project Title : Daily Calorie Tracker
'''

print("Welcome to the 'Calorie Tracker' family! \nWe're stoked to have you here. Stay \ntunned subscriber only deals and \nspecial offers.")
print("This tool help's you to track your daily calories so that you can gain or loose weight accordingly to stay fit. ")

n = int(input(" enter a no. of elements"))
data = {}
for i in range(n):
    key = input("enter Meal: ")
    value = float(input("enter Calorie: "))
    data[key]=value
print("Here is complete list : ")
print(data)

print("Calorie Intake : ")
daily_calorie_intake = int(input("eneter according to your requirment chart:  "))
total_calories_intake = sum(data.values())
print(total_calories_intake)
average_calorie_per_meal = (total_calories_intake)/n
print(average_calorie_per_meal)

if (total_calories_intake > daily_calorie_intake) :
    print("Mind your step !!!")
else :
    print("Success...")

print(f"{'Meal':<10} {'Calorie':}")      
for meal, calorie_val in data.items():
    print(f"{meal:<10} {calorie_val:}")

save_report = input('Would you like to save this report? (yes/no): ').lower()
if save_report == "yes":
    filename = "calorie_log.txt"
    with open(filename, 'w', encoding="utf-8") as file:
        file.write("Daily Calorie Tracker Report")
        file.write(f"{'Meal Name':<10}{'Calories':}")
        for i in range(n):
            file.write(f"This is total calorie {total_calories_intake} ")
            file.write(f"This is average calorie {average_calorie_per_meal}")
        if total_calories_intake > daily_calorie_intake :
            file.write(f"Warning you are going out of limit.")
        else:
            file.write("Great job! You are within your daily calorie limit.")
    print(f"Report saved successfully as '{filename}'.")
else:
    print("Report not saved. TRY AGAIN!")