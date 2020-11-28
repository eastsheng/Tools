import numpy as np

# 1 bohr = 0.52917706 angstrom
bohr = 0.52917706

class UnitConvert(object):
    """docstring for Unit"""
    # bohr --> angstrom
    def Bohr_A(self,b):
        a = b*bohr
        print(b,'bohr =',a,'Angstrom')
        return a

    def Angstrom_B(self,a):
        b = a/bohr
        print(a,'Angstrom =',b,'bohr')
        return b


# ---->Main Program<----#

# Bohr >> Angstrom and Angstrom >> Bohr

# Bohr = 102.083
Angstrom = 50

units = UnitConvert()

# units.Bohr_A(Bohr)
b = units.Angstrom_B(Angstrom)

nb1 = b/51.041517181413724

print(b)


print(nb1)
