x = 0
equation = -16*x**2 + 22*x + 340
velocity = -32*x + 22
while equation != 0 and equation > 0:
    x += 0.00001
    equation = -16*x**2 + 22*x + 340
print(x, equation)