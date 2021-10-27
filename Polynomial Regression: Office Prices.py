#https://www.hackerrank.com/challenges/predicting-office-space-price/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def read_input():
    F, N = list(map(int, input().split(' ')))
    
    train_data = list()
    test_data = list()
    [train_data.append(input().split(' ')) for _ in range(0, N)]
    
    T = int(input())
    [test_data.append(input().split(' ')) for _ in range(0, T)]
    
    train_data = np.array(train_data, dtype = np.float64)
    test_data = np.array(test_data, dtype = np.float64)
    
    xtrain = train_data[:, :F]
    ytrain = train_data[:, -1]
    
    return xtrain, ytrain, test_data

def model_fit_predict(xtrain, ytrain, xtest):
    poly = PolynomialFeatures(4)
    poly_train = poly.fit_transform(xtrain)
    poly_test = poly.transform(xtest)
    
    model = LinearRegression()
    model.fit(poly_train, ytrain)
    preds = model.predict(poly_test)
    return preds

def model_pipeline_fit_predict(xtrain, ytrain, xtest):
    degree = 4
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(xtrain, ytrain)
    preds = model.predict(xtest)
    return preds

def main():
    xtrain, ytrain, xtest = read_input()
    preds = model_fit_predict(xtrain, ytrain, xtest)
    return '\n'.join(list(map(str, preds)))

if __name__ == '__main__':
    predictions = main()
    print(predictions)
    
