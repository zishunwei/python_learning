num = 0.0
squared_num = 0.0
n = int(input("number of input:"))

for i in range(n):
    a = float(input("insert value number " + str(i+1) + ":"))
    num = num + a
    squared_num = squared_num + a**2

mean = num/n
variance = squared_num/n - mean**2

print("The mean is", mean, "The variance is ", variance)
