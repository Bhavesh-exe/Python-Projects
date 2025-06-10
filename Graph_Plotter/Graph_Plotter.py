# import matplotlib.pyplot as plt

# x = [2, 4, 5]
# y = [2, 3, 6]

# plt.plot(x, y)


# plt.xlabel('X Axis')

# plt.ylabel( 'Y Axis')

# plt.title('Demo Graph ')

# plt.show()


import matplotlib.pyplot as plt

# Take input from the user for x and y values
x_input = input("Enter X values separated by spaces: ")
y_input = input("Enter Y values separated by spaces: ")

# Convert the input strings to lists of integers
x = list(map(float, x_input.strip().split()))
y = list(map(float, y_input.strip().split()))

# Check if both lists are the same length
if len(x) != len(y):
    print("Error: The number of X and Y values must be the same.")
else:
    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Graph')
    plt.show()
