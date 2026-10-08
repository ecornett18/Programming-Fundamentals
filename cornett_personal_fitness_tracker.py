# Author: Ebony Cornett
# Date: September 13, 2026
# Description: Personal Fitness Tracker
# Tier Attempted: Base Level

# Testing Results:
# 180 calories / 45 minutes = 4.0 cal/min - Low
# 300 calories / 40 minutes = 7.5 cal/min - Moderate
# 320 calories / 30 minutes = 10.7 cal/min - High
# Boundary Test: 250 calories / 50 minutes = 5.0 cal/min - Moderate
# Boundary Test: 200 calories / 20 minutes = 10.0 cal/min - High

# Functions
def calories_per_minute(calories, duration):
    rate = calories / duration
    return round(rate, 1)
def get_intensity(rate):
    if rate < 5.0:
        return "Low"
    elif rate < 10.0:
        return "Moderate"
    else:
        return "High"
    
# Main program
print("Welcome to the Personal Fitness Tracker!")
print("You will log 3 workouts.")

# Store workout data
workouts = []
for workout_number in range(1, 4):
    print(f"\n--- Workout {workout_number} ---")    
    workout_name = input("Workout name: ")
    duration = int(input("Duration (minutes): "))
    calories = int(input("Calories burned: "))
    workout = [workout_name, duration, calories]
    workouts.append(workout)
    # Calculate and display workout results    
    rate = calories_per_minute(calories, duration)
    intensity = get_intensity(rate)
    print(f"Result: {workout_name} | {duration} min | {calories} cal | {rate:.1f} cal/min | Intensity: {intensity}")
print("\nAll workouts logged. Great job staying active!")    
