from fog_simulate1 import main
x=[]
y1=[]
y2=[]
for i in range (10):
    capacity =[10*(10**(8)) for j in range(3)]
    x.append(10*(10**(10+i)))
    a,b=main(capacity)
    y1.append(a)
    y2.append(b)
print(x,y1,y2)
# Create the plot
plt.plot(x, y1, label='Standalone Fog node')
plt.plot(x, y2, label='Fog Federation')

# Add labels and title to the plot
plt.xlabel('Computational capacity per fog node')
plt.ylabel('Y-axis')
plt.title('Graph with y1 and y2 values')

# Add legend to the plot
plt.legend()

# Show the plot
plt.show()