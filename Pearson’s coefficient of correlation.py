#https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]

x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)

num_sum = sum((a - x_mean)*(b - y_mean) for a, b in zip(x, y))
dnm_sum = (sum((a - x_mean)**2 for a in x)* sum((b - y_mean)**2 for b in y))**0.5

pearsn_coeff = round(num_sum/dnm_sum, 3)

print(str(pearsn_coeff))
