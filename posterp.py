#moores 27/10
import numpy as np
import matplotlib.pyplot as plt


x = 1.5E11
y = 1
thetan = np.arctan(abs(y/x))
G = 6.67E-11  #  gravitational constant
Me = 1  #  mass earth so small not relevant
Ms = 1.988416E30   # vary this solar mass
pi = np.pi
T = 365*24*60*6  #  period, irrelevant
dt = 0.1
s0 = np.sqrt(x**2+y**2) #  radius
F0 = (G*Ms*Me)/(s0**2) #Newton law of grav.
a0 = F0/Me #F=ma
ax = 0 #x acceleration
ay = 0 #y acceleration
vx = 0 #x velocity
vy = 29784 #y velocity
s = 1.5E11 #1 AU

#create a list
x_values = []
y_values = []
#earth orbit
#change variables wrt time
for i in range (1000000):
    dt = 100
    r = np.sqrt(x**2+y**2)
    F = (G*Ms*Me)/(r**2)
    a = F/Me
    theta = np.arctan(abs(y/x))#finding angle absolute value keeps arctan positive
    ax = -a*np.cos(theta)*(x/abs(x))#abs keeps positive
    ay = -a*np.sin(theta)*(y/abs(y))
    vx = vx+ax*dt
    vy = vy+ay*dt
    x = x+vx*dt
    y = y+vy*dt
    x_values.append(x)
    y_values.append(y)

#pulsar orbit
xa_values = []
ya_values = []

x = 1.5E11
y = 1
thetan = np.arctan(abs(y/x))
G = 6.67E-11
Me = 1
Ms = 1.988416E30  # vary this
pi = np.pi
T = 365*24*60*6
dt = 0.1
s0 = np.sqrt(x**2+y**2)
F0 = (G*Ms*Me)/(s0**2)
a0 = F0/Me
ax = 0
ay = 0
vx = 0
vy = 29784
s = 1.5E11
for i in range (1000000):
    dt = 100
    r = np.sqrt(x**2+y**2)
    F = (G*1.4*Ms*Me)/(r**2) #change sun mass to pulsar mass
    a = F/Me
    theta = np.arctan(abs(y/x))
    ax = -a*np.cos(theta)*(x/abs(x))
    ay = -a*np.sin(theta)*(y/abs(y))
    vx = vx+ax*dt
    vy = vy+ay*dt
    x = x+vx*dt
    y = y+vy*dt
    xa_values.append(x)
    ya_values.append(y)

plt.plot(x_values, y_values,label='sun orbit')
plt.plot(xa_values, ya_values, 'xkcd:bright pink', label='pulsar orbit')
plt.plot(0,0,'ro', label='pulsar')
plt.legend(loc='lower right')
plt.grid()
plt.axis('equal')
plt.title("Orbit of Earth and Star")
plt.xlabel("X displacement")
plt.ylabel("Y displacement")
plt.show()


x = 1.5E11
y = 1
thetan = np.arctan(abs(y/x))
G = 6.67E-11
Me = 1
Ms = 1.988416E30  # vary this
pi = np.pi
T = 365*24*60*6
dt = 0.1
s0 = np.sqrt(x**2+y**2)
F0 = (G*Ms*Me)/(s0**2)
a0 = F0/Me
ax = 0
ay = 0
vx = 0
vy = 29784
s = 1.5E11
L = 0.9 #not used
#luminosity
x_values = []
y_values = []
z_values = [] #inensity of light in solar luminosities
r_values = [] #distanc in metres
MA_values =[] #apparent magnitude

for i in range(1000000):
    dt = 100
    r = np.sqrt(x**2+y**2)
    K = ((1.2149)/(4*np.pi*(r**2)))
    MA= 4.53+(5*(np.log(r*(1/(3.0857E17)))))
    F = (G*1.4*Ms*Me)/(r**2)
    a = F/Me
    theta = np.arctan(abs(y/x))
    ax = -a*np.cos(theta)*(x/abs(x))
    ay = -a*np.sin(theta)*(y/abs(y))
    vx = vx+ax*dt
    vy = vy+ay*dt
    x = x+vx*dt
    y = y+vy*dt
    x_values.append(x)
    y_values.append(y)
    z_values.append(K)
    r_values.append(r)
    MA_values.append(MA)

plt.plot ( r_values, z_values,'xkcd:bright pink')
#plt.legend()
plt.grid()
#plt.axis('equal')
plt.title("Intensity of Light from Pulsar observed from Earth")
plt.xlabel("Distance from Pulsar (m)")
plt.ylabel("Solar Luminosities")

plt.show()

plt.plot ( r_values , MA_values)
plt.grid()
#plt.axis('equal')
plt.title('Magnitude of Brightness of Pulsar with respect to distance')
plt.xlabel("Distance from Pulsar (m)")
plt.ylabel('Apparent Magnitude')
plt.show()