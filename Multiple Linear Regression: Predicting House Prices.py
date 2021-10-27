#https://www.hackerrank.com/challenges/predicting-house-prices/submissions/code/240219193
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn.linear_model import LinearRegression

def read_input():
    train_data = list()
    test_data = list()
    F, N = list(map(int, input().split(' ')))
    
    [train_data.append(input().split(' ')) for _ in range(0, N)]
    
    T = int(input())
    [test_data.append(input().split(' ')) for _ in range(0, T)]
    
    train_data = np.array(train_data, dtype = np.float64)
    test_data = np.array(test_data, dtype = np.float64)
    
    xtrain = train_data[:, :F]
    ytrain = train_data[:, -1]
    
    return xtrain, ytrain, test_data

def model_fit_predict(xtrain, ytrain, xtest):
    model = LinearRegression()
    model.fit(xtrain, ytrain)
    preds = model.predict(xtest)
    return preds

def main():
    xtrain, ytrain, xtest = read_input()
    house_price = model_fit_predict(xtrain, ytrain, xtest)
    return '\n'.join(list(map(str, house_price)))

if __name__ == '__main__':
    predtictions = main()
    print(predtictions)
