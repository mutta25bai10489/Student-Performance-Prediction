import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model():
    data = pd.read_csv('data.csv')
    
    X = data[['hours', 'attendance', 'previous_marks']]
    y = data['final_marks']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model
