import pylab as plt


mySamples= []
myLinear= []
myQuadratic= []
myCubic= []
myExponential= []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)


# Use .figure(Arg) to graph each one separately
# Creates a new display with that name if one does not already exist
plt.figure('lin vs qua')
plt.title('lin vs qua')
# Generate the plot, plt.plot(x, y). Lists must be of the same lengths
plt.plot(mySamples, myLinear, label='Linear')


# Use the same name. Will show up on the same graph. Same thing as not calling at all.
plt.figure('lin vs qua')
plt.xlabel('Samples')
plt.ylabel('Function')
# Set the limit of y values. Set the range on y axis
plt.ylim(0, 50)
plt.plot(mySamples, myQuadratic, label='Quadratic', c='r')
plt.legend(loc='upper left')

plt.figure('cube')
plt.plot(mySamples, myCubic, label='Cube')
# Clear the window
plt.clf()


plt.figure('expo')
plt.plot(mySamples, myExponential, label='Exponential')

# Add graph to existing figures
# Reopen the old figure and modify it
plt.figure('cube')
plt.plot(mySamples, [y**1.2 for y in range(0, 30)], label='???')
plt.xlabel('Samples')
plt.ylabel('Cube Function')
plt.legend()



plt.show()

