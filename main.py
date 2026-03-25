from model import train_model

model = train_model()

print("Enter student details:")
hours = float(input("Study Hours: "))
attendance = float(input("Attendance (%): "))
previous_marks = float(input("Previous Marks: "))

prediction = model.predict([[hours, attendance, previous_marks]])

print(f"Predicted Final Marks: {prediction[0]:.2f}")
