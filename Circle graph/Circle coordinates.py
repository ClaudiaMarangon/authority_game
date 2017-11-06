import math
import numpy as numpy
import csv


x_coord = []
x_coord.append(0)
y_coord = []
y_coord.append(10)
x = int(1)
while x<=1000:
    z = x/float(100)
    def circle(var):
        y = math.sqrt(100 - var**2) 
        return y
    x_coord.append(z)
    y_coord.append(circle(z))
    x = x + 1
rows = []
length = len(x_coord)

#creating the rows array with all data for the circle
for var in range(0, length):
    row_var = [x_coord[var], y_coord[var]]
    rows.append(row_var)
print (rows)

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
   
