# Author: Ebony Cornett
# Date: September 6, 2026
# Description: Student Grade Analyzer
# Tier Attempted: Base Level

# Testing Results:
# High Performer: 95, 98, 92, 97, 100 -> Average: 96.4, Grade: A
# Average Performer: 75, 82, 70, 68, 80 -> Average: 75.0, Grade: C
# Struggling Student: 55, 48, 60, 52, 58 -> Average: 54.6, Grade: F
# Boundary Test: 90, 80, 70, 60, 50 -> Average: 70.0, Grade: C

print("Welcome to the Student Grade Analyzer!")
# Ask for the student's name
student_name = input("Enter the student's name: ").strip().title()
# Ask for the student's five quiz scores
quiz1 = int(input("Enter Quiz 1 score: "))
quiz2 = int(input("Enter Quiz 2 score: "))
quiz3 = int(input("Enter Quiz 3 score: "))
quiz4 = int(input("Enter Quiz 4 score: "))
quiz5 = int(input("Enter Quiz 5 score: "))
# Store the quiz scores in a list
quiz_scores = [quiz1, quiz2, quiz3, quiz4, quiz5]
# Store the letter grade labels in a tuple
grade_labels = ("A", "B", "C", "D", "F")
# Calculate the average of the five quiz scores
average = sum(quiz_scores) / len(quiz_scores)
# Determine the letter grade based on the average score
if average >= 90:
    letter_grade = grade_labels[0]
elif average >= 80:
    letter_grade = grade_labels[1]
elif average >= 70:
    letter_grade = grade_labels[2]
elif average >= 60:
    letter_grade = grade_labels[3]
else:
    letter_grade = grade_labels[4]
# Create a personalized message based on the letter grade
if letter_grade == "A":
    message = "Excellent work!"
elif letter_grade == "B":
    message = "Great job! Keep up the solid effort."
elif letter_grade == "C":
    message = "Good work! Keep working hard."
elif letter_grade == "D":
    message = "Consider visiting office hours for extra help."
else:
    message = "Consider visiting office hours for extra help."
# Display the results
print("===== Grade Report =====")
print(f"\nStudent: {student_name}")
print(f"Quiz Scores: {quiz_scores}")
print(f"Average Score: {average:.1f}")
print(f"Letter Grade: {letter_grade}")
print(f"Message: {message}")
print("========================")