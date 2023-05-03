from fog_simulate1 import main
import matplotlib.pyplot as plt
x=[]
y1=[]
y2=[]
for i in range (100):
    capacity =[10*(2*i+1)*(10**(8)) for j in range(3)]
    x.append(10*(2*i+1)*(10**(9)))
    a,b=main(capacity)
    y1.append(a)
    y2.append(b)
print(x,y1,y2)
# Create the plot
plt.plot(x, y1, label='Standalone Fog node',alpha =0.5)
plt.plot(x, y2, label='Fog Federation',alpha= 0.5,linestyle='--')

# Add labels and title to the plot
plt.xlabel('Computational capacity per fog node (CPU cycles/slot)')
plt.ylabel('Total revenue (unit price)')


# Add legend to the plot
plt.legend()

# Show the plot
plt.show()