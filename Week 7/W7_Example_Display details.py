import matplotlib.pyplot as plt


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


plt.figure('Linear vs Quadratic')

plt.subplot(211)
plt.plot(mySamples, myQuadratic, 'k--', label='Quadratic', linewidth=4)
plt.ylim(0,100)
plt.title('Quadratic')
plt.legend()

plt.subplot(212)
plt.plot(mySamples, myLinear, 'b^', label='Linear')
plt.title('Linear')
plt.ylim(0, 100)
plt.legend()





plt.figure('Cubic vs Exponential')

plt.subplot(121)
plt.plot(mySamples, myCubic, 'g--', label='Cubic', linewidth=2)
plt.title('Cubic')
plt.yscale('log')
plt.legend()


plt.subplot(122)
plt.plot(mySamples, myExponential, 'r*', label='Linear')
plt.title('Expo')
plt.yscale('log')
plt.legend()
plt.show()