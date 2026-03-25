# Student-Performance-Prediction
# Student Performance Prediction using Machine Learning

## Project Overview

This project predicts a student's final performance (marks) based on key academic factors such as study hours, attendance percentage, and previous marks. The system uses a machine learning model to analyze patterns in the data and generate predictions.

The objective of this project is to demonstrate the practical application of machine learning techniques in the education domain.

---

## Features

* Predict student final marks based on input parameters
* Uses a simple and efficient machine learning model
* Command-line based execution
* Easy to understand and modify

---

## Machine Learning Algorithm Used

* Linear Regression

Linear Regression is used to model the relationship between input features (study hours, attendance, previous marks) and the output (final marks).

---

## Technologies Used

* Python
* Pandas
* Scikit-learn

---

## Project Structure

```
student-performance-prediction/
│
├── data.csv              # Dataset
├── model.py              # Model training code
├── main.py               # Main execution file
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## Installation and Setup

### Step 1: Clone the Repository

```
git clone https://github.com/your-username/student-performance-prediction.git
cd student-performance-prediction
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

---

## How to Run the Project

Run the following command in the terminal:

```
python main.py
```

---

## Input Example

Enter student details when prompted:

```
Study Hours: 5
Attendance (%): 75
Previous Marks: 65
```

---

## Output Example

```
Predicted Final Marks: 68.50
```

---

## Model Details

* The dataset is split into training and testing sets
* The model is trained using Linear Regression
* Predictions are made based on learned relationships

---

## Dataset Description

The dataset contains the following features:

* hours → Number of hours studied
* attendance → Attendance percentage
* previous_marks → Marks obtained previously
* final_marks → Target variable (predicted output)

The dataset used in this project is synthetically generated based on realistic academic trends.

---

## Evaluation

The model performance can be evaluated using:

```
model.score(X_test, y_test)
```

---

## Assumptions

* Higher study hours generally lead to better performance
* Better attendance improves final marks
* Previous academic performance influences future results

---

## Future Improvements

* Add more features such as sleep hours and assignment scores
* Implement advanced models such as Decision Tree and Random Forest
* Add graphical visualization
* Build a web interface using Flask or Streamlit

---

## How to Use

1. Install dependencies
2. Run the project
3. Enter input values
4. View predicted output

---

## Contribution

This project is developed as part of an academic submission. Contributions are not required but suggestions are welcome.

---

## License

This project is for educational purposes only.

---

## Acknowledgement

This project is created as part of the BYOP (Bring Your Own Project) submission for the AI/ML flipped course.
