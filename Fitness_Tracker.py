# Classes
class User:
    def __init__(self, name, age, weight, height, sex, activity_level):
        self.name = name
        self.age = age
        self.weight = weight # in kg
        self.height = height # in cm
        self.sex = sex 
        self.activity_level = activity_level

    def calculate_bmr(self):
        # Mifflin-St Jeor Equation
        if self.sex == "male":
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5 
        elif self.sex == "female":
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        
        activity_multiplier = {
            "sedentary": 1.2, 
            "lightly active": 1.375,
            "moderately active": 1.55,
            "very active": 1.725 
            }
        return bmr * activity_multiplier[self.activity_level]
    
class DayLog:
    def __init__(self, steps, calories_burned, water_intake):
        self.steps = steps
        self.caloires_burned = calories_burned
        self.water_intake = water_intake

# Functions
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a nunber.")

def log_daily_activity():
    steps = get_positive_number("Enter the number of steps you walked today: ")
    calories_burned = get_positive_number("Enter the calories you burned today: ")
    water_intake = get_positive_number("Enter the litres of water you drank today: ")
    return DayLog(steps, calories_burned, water_intake)

def main():
    print("Welcome to the Personalized Fitness Tracker!")
    name = input("Enter your name: ")
    sex  = input("Enter you sex (male or female): ").strip().lower()

    while sex not in ["male", "female"]:
        print("Invalid sex option. Please choose from male or female.")
        sex  = input("Enter you sex (male or female): ").strip().lower()

    age = get_positive_number("Enter your age: ")
    weight = get_positive_number("Enter your weight (kg): ")
    height = get_positive_number("Enter your height (cm): ")

    print("Activity Levels: sedentary, lightly active, moderately active, very active")
    activity_level = input("Enter you activity level: ").strip().lower()
    while activity_level not in ["sedentary", "lighly active", "moderately active", "very active"]:
        print("Invalid activity level. Please choose from sedentary, lightly active, moderately active, very active.")
        activity_level = input("Enter you activity level: ").strip().lower()

    user = User(name, age, weight, height, sex, activity_level)
    daily_calories = user.calculate_bmr()
    print(f"\n{name}, your daily calorie requirement is approximately {daily_calories:.2f} calories.\n")

    #Track daily progress 
    logs = []
    while True:
        print("\n1. Log today's activity")
        print("2. View weekly summary")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            log = log_daily_activity()
            logs.append(log)
            print("\nActivity logged successfully!")

        elif choice == "2":
            if logs:
                print("\nWeekly Summary:")
                total_steps = sum(log.steps for log in logs)
                total_caloires = sum(log.caloires_burned for log in logs)
                total_water = sum(log.water_intake for log in logs)
                print(f"Total Steps: {total_steps}")
                print(f"Total Calories Burned: {total_caloires}")
                print(f"Total Water Consumed: {total_water} liters")
            else:
                print("No activity logged yet.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()



