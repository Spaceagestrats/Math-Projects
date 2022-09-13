import math

vector = (input("Input a vector of this format ('x','y')"))
vector_points = vector.split(',')
for point in vector_points:
    vector_points[vector_points.index(point)] = float(point)
(x),(y) = vector_points
vector_magnitude = math.sqrt(x*x+y*y)
print(vector_magnitude)