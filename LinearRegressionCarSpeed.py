import numpy as np
import random as r
import matplotlib.pyplot as plt
import csv


inp = []
out = []
sampleSize = int(1E5)


def generate():
    file = open("Data.csv", 'w', newline='')
    writer = csv.writer(file)
    for i in range(sampleSize):
        age = (10 * r.random())
        topSpeed = ((15 - age) * (8 + (2 * r.random())))
        writer.writerow([age, topSpeed])
    file.close()
    return


def read():
    file = open("Data.csv", 'r')
    reader = csv.reader(file)
    for i in reader:
        inp.append(float(i[0]))
        out.append(float(i[1]))
    file.close()
    return


generate()  # to generate new csv file containing data if not provided already
read()  # reads a file named Data.csv where column A is input and column B is output
age = np.array(inp)
top_speed = np.array(out)

mean_age = np.mean(age)
mean_top_speed = np.mean(top_speed)
numerator = np.sum((age - mean_age) * (top_speed - mean_top_speed))
denominator = np.sum((age - mean_age) ** 2)
slope = numerator / denominator
intercept = mean_top_speed - (slope * mean_age)

testInp = float(input("Enter car age - "))
print(f"The top speed is {slope * testInp + intercept}")

predictedOut = []
for i in inp:
    predictedOut.append(intercept + slope * i)
plt.scatter(inp, out)
plt.plot(inp, predictedOut, 'r')
plt.show()
