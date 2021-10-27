#https://www.hackerrank.com/challenges/correlation-and-regression-lines-7/submissions/code/240227574
x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]
size = len(x)
x_mean = sum(x)/size
y_mean = sum(y)/size

num_sum = sum([(a -x_mean)*(b - y_mean) for a, b in zip(x, y)])
den_sum = sum([(a - x_mean)**2 for a in x])
slope = round(num_sum/den_sum, 3)
print(str(slope))
