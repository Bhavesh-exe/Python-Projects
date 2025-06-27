import matplotlib.pyplot as plt

Take input from the user for x and y values
x_input = input("Enter X values separated by spaces: ")
y_input = input("Enter Y values separated by spaces: ")

Convert the input strings to lists of integers
x = list(map(float, x_input.strip().split()))
y = list(map(float, y_input.strip().split()))


if len(x) != len(y):
    print("Error: The number of X and Y values must be the same.")
else:
    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Graph')
    plt.show()
