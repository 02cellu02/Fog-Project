import matplotlib.pyplot as plt

# Generate x, y1, and y2 data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Create the plot
plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')

# Add labels and title to the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph with y1 and y2 values')

# Add legend to the plot
plt.legend()

# Show the plot
plt.show()