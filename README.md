# Student Final Marks Predictor

College Project | Academic Year 2025–26  

## Student Details
Name: M.Ganesh Kumar
Reg No: 25BAI10489
Course: CSA-2001


---

## Overview
The Student Final Marks Predictor is a Machine Learning application built using Python and Scikit-learn. It predicts a student’s final marks based on study habits and past academic performance.  

This project uses a Linear Regression model to find the relationship between study hours, attendance, previous marks, and final marks. It is a practical implementation of supervised learning for academic performance analysis.  

---

## Features
- Predictive Analysis: Estimates final marks based on input values  
- Trained Model: Uses dataset (data.csv) for training and testing  
- User-Friendly CLI: Simple command-line interface for predictions  
- Data Handling: Uses pandas for efficient data processing  

---

## Technical Stack
Language: Python  

Libraries Used:  
pandas for data manipulation  
scikit-learn for machine learning model  
numpy for numerical operations  

---

## Dataset Structure
The model uses a dataset file named data.csv with the following columns:

- hours: Number of study hours  
- attendance: Attendance percentage  
- previous_marks: Marks from previous exams  
- final_marks: Target value to be predicted  

---

## How to Run
1. Clone the repository  
   git clone https://github.com/your-username/student-marks-predictor.git  

2. Install required libraries  
   pip install pandas scikit-learn  

3. Ensure data.csv is in the same folder  

4. Run the script  
   python predictor.py  

---

## Logic and Methodology
- Dataset is split into training (80%) and testing (20%) using train_test_split  
- LinearRegression model is trained on the dataset  
- User inputs are taken for prediction  
- Model outputs predicted final marks  

---

## Conclusion
This project shows how machine learning can be used to analyze and predict student performance. It helps understand the impact of study habits on final results.  

---

## Future Enhancements
- Add graphical user interface (GUI)  
- Improve dataset with more features  
- Deploy as a web application

