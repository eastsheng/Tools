import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# integrate dos :x=fre,y=dos
def Integrate_dos(x, y):
    y_integrate = integrate.cumtrapz(y, x)
    # print(y_integrate)
    return y_integrate
# x=frequency,y1=dos_eq,y2=dos_ne,T_eq=temperature of equilibrium status
def freT(x,y1,y2,T_eq):
    T = T_eq*(Integrate_dos(x, y1)/Integrate_dos(x, y2))
    return T

# plot 
def plotft(x, y, savefig=True, saveft=True, xmin=0, xmax=20):
    plt.rc('font', family='Times New Roman')
    fig,ax = plt.subplots(figsize = (8,6))
    fig.subplots_adjust(bottom=0.15,left=0.15)
    plt.plot(x,y,'b-')
    plt.xlabel("Frequency (THz)", size=24)
    plt.ylabel("Temperature (K)", size=24)
    plt.xticks(size=22)
    plt.yticks(size=22)
    plt.xlim(xmin, xmax)
    # plt.ylim(ymin=0, ymax=300)
    if savefig == True:
        plt.savefig('fre_T.png',dpi=300)
    plt.show()

    if saveft==True:
        lx = len(x)
        ly = len(y)
        ft = np.hstack((x.reshape(lx,1),y.reshape(ly,1)))
        np.savetxt('fre_T.txt',ft,'%f %f')
    return


##################----Main Program----####################
print("-----------Start!-----------")
# equilibrium temperature
T_eq = 300 #K
# read equilibrium and noequilibrium temperature
vdos_eq = np.loadtxt('VDOS_eq.normalized.dat',skiprows=2)
vdos_ne = np.loadtxt('VDOS_ne.normalized.dat',skiprows=2)

vdos_fre = vdos_eq[:,0]

vdos_eq_x = vdos_eq[:, 1]
vdos_eq_y = vdos_eq[:, 2]
vdos_eq_z = vdos_eq[:, 3]
vdos_eq_av = vdos_eq[:, 4]

vdos_ne_x = vdos_ne[:, 1]
vdos_ne_y = vdos_ne[:, 2]
vdos_ne_z = vdos_ne[:, 3]
vdos_ne_av = vdos_ne[:, 4]

# calculating
T = freT(vdos_fre, vdos_eq_av, vdos_ne_av, T_eq)

# print(T.shape)
# plot
savefig = True
# savetxt
saveft = True
xmin, xmax = 0, 20

plotft(vdos_fre[1:], T, savefig, saveft, xmin, xmax)

print("-----------All Done!-----------")